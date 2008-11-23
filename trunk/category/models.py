from django.db import models
from django.core import urlresolvers
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.contrib.sites.models import Site
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

# Create your models here.
class CategoryManager(models.Manager):
    def get_children_for_pk(self, pk):
        return self.filter(root_pk=pk)
        
class BaseCategoryAbstractModel(models.Model):
    """
    An abstract base class that any custom comment models probably should
    subclass.
    """

    # Content-object field
    content_type   = models.ForeignKey(ContentType,
            related_name="content_type_set_for_%(class)s")
    object_pk      = models.TextField(_('object ID'))
    content_object = generic.GenericForeignKey(ct_field="content_type", fk_field="object_pk")

    # Metadata about the comment
    site        = models.ForeignKey(Site)

    class Meta:
        abstract = True

    def get_content_object_url(self):
        """
        Get a URL suitable for redirecting to the content object.
        """
        return urlresolvers.reverse(
            "category-url-redirect",
            args=(self.content_type_id, self.object_pk)
        )
        
class Category(BaseCategoryAbstractModel):
    """
    Category
    """
    user          = models.ForeignKey(User, blank=True, null=True, related_name="%(class)s_category")
    name          = models.CharField(_('name'), max_length=50)
    parent        = models.ForeignKey('self', verbose_name=_('parent category'), null=True,blank=True,related_name='child')
    root_pk       = models.PositiveSmallIntegerField(_('root pk'), blank=True,null=True)
    display_order = models.PositiveSmallIntegerField(_('Order'), default=1)
    
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
        
        
