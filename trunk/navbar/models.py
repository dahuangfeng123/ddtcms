"""NavBar models for building and managing dynamic site navigation
"""
from django.db import models
from django.conf import settings
from django.contrib.auth.models import Group
#from django.core.validators import ValidationError
from django.core.cache import cache
from django.db.models.query import Q
from django.utils.translation import ugettext_lazy as _
import re

USER_TYPE_CHOICES = [
    ('A', _('Anonymous')),
    ('L', _('Logged In')),
    ('S', _('Staff')),
    ('X', _('Superuser')),
]

SELECTION_TYPE_CHOICES = [
    ('N', _('Never')),
    ('E', _('Exact')),
    ('P', _('ExactOrParent')),
    ('A', _('OnPathOrParent (default)'))
]

url_re = re.compile(r'^(https?://([a-zA-Z0-9]+\.)+[a-zA-Z0-9]([:@][a-zA-Z0-9@%-_\.]){0,2})?/\S*$')

def IsNotCircular(field_data, all_data):
    if 'id' not in all_data or all_data['id'] is None or not all_data['parent']:
        return
    cid = int(all_data['id'])
    pid = int(all_data['parent'])
    try:
        while pid:
            parent = NavBarItem.objects.get(pk=pid)
            pid = parent.parent_id
            if pid is None: return
            if pid == cid:
                raise ValidationError(u"Creates a cyclical reference.")
    except NavBarItem.DoesNotExist:
        raise ValidationError("Could not find parent: " + str(pid) +
                              " Corrupt DB?")

def isValidLocalOrServerURL(field_data, all_data):
    if not url_re.search(field_data):
        raise ValidationError(u"A valid URL is required.")
    ## RED_FLAG: add signals based local check (from request object)
    if field_data.startswith('http'):
        import urllib2
        try:
            from django.conf import settings
            URL_VALIDATOR_USER_AGENT = settings.URL_VALIDATOR_USER_AGENT
        except (ImportError, EnvironmentError):
            # It's OK if Django settings aren't configured.
            URL_VALIDATOR_USER_AGENT = 'Django (http://www.djangoproject.com/)'
        headers = {
            "Accept": "text/xml,application/xml,application/xhtml+xml,"
                      "text/html;q=0.9,text/plain;q=0.8,image/png,*/*;q=0.5",
            "Accept-Language": "en-us,en;q=0.5",
            "Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.7",
            "Connection": "close",
            "User-Agent": URL_VALIDATOR_USER_AGENT,
        }
        try:
            req = urllib2.Request(field_data, None, headers)
            u = urllib2.urlopen(req)
        except ValueError:
            raise ValidationError(u'Enter a valid URL.')
        except: # urllib2.URLError, httplib.InvalidURL, etc.
            raise ValidationError(u'This URL appears to be a broken link.')

class NavBarRootManager(models.Manager):
    def get_query_set(self):
        all = super(NavBarRootManager, self).get_query_set()
        return all.filter(parent__isnull=True)


class NavBarItem(models.Model):
    name   = models.CharField(max_length=50,
                              help_text=_("text seen in the menu"))
    title  = models.CharField(max_length=50, blank=True,
                              help_text=_("mouse hover description"))
    url    = models.CharField(max_length=200)#, validator_list=[isValidLocalOrServerURL])
    order  = models.IntegerField(default=0)
    parent = models.ForeignKey('self', related_name='children',
                               blank=True, null=True)#,validator_list=[IsNotCircular])

    ## advanced permissions
    path_type = models.CharField(_('path match type'), max_length=1,
                                 choices=SELECTION_TYPE_CHOICES, default='A',
                                 help_text=_("Control how this element is "
                                             "marked 'selected' based on the "
                                             "request path."))
    user_type = models.CharField(_('user login type'), max_length=1,
                                 choices=USER_TYPE_CHOICES,
                                 default=USER_TYPE_CHOICES[0][0])
    groups    = models.ManyToManyField(Group, null=True, blank=True)

    objects = models.Manager()
    top     = NavBarRootManager()

    class Meta:
        verbose_name = _('navigation bar element')
        verbose_name_plural = _('navigation bar elements')
        #order_with_respect_to = 'parent' # doesn't woth with self relations
        ordering = ('parent__id', 'order', 'id','name')

    def __unicode__(self):
        return self.name

    def save(self):
        cache.delete('site_navtree')
        cache.delete('site_navtree_super')
        return super(NavBarItem, self).save()

def Qperm(user=None):
    exQ = Q()
    if user is None or user.is_anonymous():
        exQ = Q(user_type__exact = 'A') & Q(
            groups__isnull=True)
    elif user.is_superuser:
        pass
    elif user.is_staff:
        exQ = (Q(user_type__exact = 'A') | Q(user_type__exact = 'L') |
               Q(user_type__exact = 'S')) & (
                    Q(groups__in=user.groups.all()) | Q(groups__isnull=True))
    else:
        exQ = (Q(user_type__exact = 'A') | Q(user_type__exact = 'L')) & (
                    Q(groups__in=user.groups.all()) | Q(groups__isnull=True))
    return exQ

def generate_navtree(user=None, maxdepth=-1):
    if maxdepth == 0: return [] ## silly...
    permQ = Qperm(user)
    urls = {}
    def navent(ent, invdepth, parent):
        current = {'name': ent.name, 'title': ent.title, 'url': ent.url,
                   'selected': False, 'path_type': ent.path_type, 'parent': parent}
        urls.setdefault(ent.url, current)
        current['children'] = navlevel(ent.children, invdepth-1, current)
        return current
    def navlevel(base, invdepth, parent=None):
        if invdepth == 0 : return []
        return [ navent(ent, invdepth, parent)
                        for ent in base.filter(permQ).distinct() ]
    tree = navlevel(NavBarItem.top, maxdepth)
    urls = sorted(urls.iteritems(), key=lambda x: x[0], reverse=True)
    return {'tree': tree, 'byurl': urls}

def get_navtree(user=None, maxdepth=-1):
    cachename = 'site_navtree'
    timeout = 60*60*24
    if user is not None and not user.is_anonymous():
        if user.is_superuser:
            cachename = 'site_navtree_super'
        else:
            cachename = 'site_navtree_' + str(user.id)
            timeout = 60*15
    data = cache.get(cachename)
    if data is None:
        data = generate_navtree(user, maxdepth)
        cache.set(cachename, data, timeout)
    return data

def get_navbar(user=None):
    return NavBarItem.top.filter(Qperm(user))
