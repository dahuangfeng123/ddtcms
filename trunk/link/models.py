from django.db import models
import datetime
from django.contrib.contenttypes import generic
from ddtcms.category.models import Category
from django.utils.translation import ugettext_lazy as _


# attempt to load the django-tagging TagField from default location,
# otherwise we substitude a dummy TagField.
try:
    from tagging.fields import TagField
    tagfield_help_text = _('Separate tags with spaces, put quotes around multiple-word tags.')
except ImportError:
    class TagField(models.CharField):
        def __init__(self, **kwargs):
            default_kwargs = {'max_length': 255, 'blank': True}
            default_kwargs.update(kwargs)
            super(TagField, self).__init__(**default_kwargs)
        def get_internal_type(self):
            return 'CharField'
    tagfield_help_text = _('Django-tagging was not found, tags will be treated as plain text.')

# Create your models here.

class Link(models.Model):
    name          = models.CharField(max_length=200)
    #category      = generic.GenericRelation(Category)
    category      = models.ForeignKey(Category)
    url           = models.URLField(max_length=255,default='http://')
    domain        = models.CharField(null=True,blank=True,max_length=255,help_text='like "sohu.com" in "www.sohu.com",or IP:"127.0.0.1"')
    slug          = models.SlugField(null=True,blank=True,help_text='Automatically built From the domain.')
    notes         = models.TextField(null=True,blank=True)
    pub_date      = models.DateTimeField(null=True,blank=True,default=datetime.datetime.now)
    tags          = TagField(help_text=tagfield_help_text, verbose_name=_('tags'))
    
    class Meta:
        verbose_name = _('Link')
        verbose_name_plural = _('Links')



    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return self.url