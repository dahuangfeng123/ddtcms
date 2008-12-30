from django.db import models
from django.core import urlresolvers
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.contrib.sites.models import Site
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from ddtcms.category.managers import CategoryManager

'''
 BaseCategoryAbstractModel learn from comments
 Category learn from djangotdd categories ,use google search this can find this app
 
'''
class BaseCategoryAbstractModel(models.Model):
    """
    An abstract base class that any custom comment models probably should
    subclass.
    """

    # Content-object field
    content_type   = models.ForeignKey(ContentType,related_name="content_type_set_for_%(class)s")

    # Metadata about the comment
    site        = models.ForeignKey(Site)

    class Meta:
        abstract = True


        
class Category(BaseCategoryAbstractModel):
    """
    Category
    """
    user          = models.ForeignKey(User, blank=True, null=True, related_name="%(class)s_category")
    name          = models.CharField(_('name'), max_length=50)
    #slug          = models.SlugField(max_length=50)
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
        
        
