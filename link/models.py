from django.db import models
import datetime
from django.contrib.auth.models import User
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
class Category(models.Model):
	user          = models.ForeignKey(User, blank=True, null=True,related_name="link_categories")
	name          = models.CharField(_('name'), max_length=50)
	slug          = models.SlugField(max_length=50,help_text='alias to the name,use english')
	parent        = models.ForeignKey('self',null=True,blank=True,related_name='link_category_child')
	depth         = models.PositiveSmallIntegerField(_("category's depth"), blank=True,null=True)
	display_order = models.PositiveSmallIntegerField(_('order'), default=1)
	
	
	class Meta:
		verbose_name = _('Link Category')
		verbose_name_plural = _('Link Categories')


    
	def __unicode__(self):
		return self.name   
 
    
	def get_children(self):
		return self.link_category_child.all()
	
	def is_root(self):
		if self.parent == None:
			return True
		return False
		
	def get_absolute_url(self):
		return "/link/category/%s/" %  self.slug
		
class Link(models.Model):
    title         = models.CharField(max_length=200)
    category      = models.ForeignKey(Category,blank=True,null=True)
    url           = models.URLField(max_length=255,default='http://',verify_exists=False)
    domain        = models.CharField(null=True,blank=True,max_length=255,help_text='like "sohu.com" in "www.sohu.com",or IP:"127.0.0.1"')
    slug          = models.SlugField(null=True,blank=True,help_text='Automatically built From the domain.')
    notes         = models.TextField(null=True,blank=True)
    pub_date      = models.DateTimeField(null=True,blank=True,default=datetime.datetime.now)
    tags          = TagField(help_text=tagfield_help_text, verbose_name=_('tags'))
    
    class Meta:
        verbose_name = _('Link')
        verbose_name_plural = _('Links')

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return self.url