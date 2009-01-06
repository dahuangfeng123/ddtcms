from django.db import models
from django.core import urlresolvers
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from ddtcms.category.managers import CategoryManager

'''

 Category learn from djangotdd categories ,use google search this can find this app
 
'''


class Outline(models.Model):
	"""
	A Outline is a "tree" of categories.
	"""
	content_type   = models.ForeignKey(ContentType,related_name="content_type_set_for_%(class)s")
	name           = models.CharField(max_length=255, help_text="The name of a category tree. For example, a hierarchy of categories of beer might be called 'Beer'.")
	slug           = models.SlugField(unique=True, help_text="A URL-friendly version of the name. Auto-populated from name.")

	
  
	class Meta:
		verbose_name = "Category Outline"
		verbose_name_plural = "Category Outlines"
		
	def __unicode__(self):
		return u"%s" % self.name
      
	@property
	def top_level_categories(self):
		return self.categories.filter(parent__isnull=True)
	
	def save(self, force_insert=False, force_update=False):
		"""
		Update any top level child categories to reflect new path.
		This will cascade down to lower levels, as categories will automatically
		re-save their children.
		"""
		super(Outline, self).save(force_insert=force_insert, force_update=force_update)
		for category in self.top_level_categories:
			category.save()


class Category(models.Model):
    """
    Category
    """
    outline       = models.ForeignKey(Outline, 
                                      verbose_name='Outline',
                                      related_name='categories',
                                      help_text="The outline this category belongs to.",
                                      default=1)
    user          = models.ForeignKey(User, blank=True, null=True, related_name="categories")
    name          = models.CharField(_('name'), max_length=50)
    slug          = models.SlugField(max_length=50,help_text='alias to the name,use english')
    parent        = models.ForeignKey('self',null=True,blank=True,related_name='category_child')
    root_pk       = models.PositiveSmallIntegerField(_("root category's pk"), blank=True,null=True)
    display_order = models.PositiveSmallIntegerField(_('order'), default=1)
    
    objects = CategoryManager()

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Category')

    def save(self, force_insert=False, force_update=False):
            self.root_pk = self.get_root_pk()
            super(Category, self).save(force_insert, force_update)
    
    def __unicode__(self):
        return self.name
    
    def get_root_pk(self):
        if not self.is_root():
            return self.parent.get_root_pk()
        else:
            return self.pk
    
    def get_children(self):
        return self.category_set.all()
    
    def is_root(self):
        if self.parent == None:
            return True
        return False
        
    #def get_absolute_url(self):
    #    return "/%s/category/%s/" % (content_type.app_label,self.slug)
        
        
