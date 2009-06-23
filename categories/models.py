
from django.db.models import signals
from django.dispatch import dispatcher
from django.db import models, backend, connection
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import ugettext_lazy as _

from categories.managers import CategoryManager

class Category(models.Model):
    """
    A category that can belong to itself and contains arbitrarty objects 
    through CategoryItem.
    """
    parent = models.ForeignKey('self', null=True, blank=True,
        related_name='children')
    lft = models.PositiveIntegerField(null=True, db_index=True, editable=False)
    rgt = models.PositiveIntegerField(null=True, editable=False)
    
    name = models.CharField(_('Name'), max_length=150)
    slug = models.SlugField(_('Slug'))
    sort_order = models.IntegerField(_('Sort Order'), default=0)
    
    objects = CategoryManager()
    
    class Meta:
        db_table='categories_category'
        verbose_name_plural = _('categories')
        unique_together = ('parent', 'name',)
    
    def get_path(self, **kwargs):
        return Category.objects.get_path(self, **kwargs)
    
    def get_tree(self, **kwargs):
        return Category.objects.get_tree(self, **kwargs)
    
    def breadcrumbs(self, field=None, delimiter=u' :: '):
        return delimiter.join([getattr(c, field or 'name') for c in self.get_path()])
    
    def num_descendants(self):
        return Category.objects.num_descendants(self)
        
    def __repr__(self):
        return '<Category %s>' % self
    
    def __unicode__(self):
        return self.name
    
    def get_absolute_url(self):
        return u'%s/' % self.breadcrumbs('slug', '/')

class CategoryItem(models.Model):
    """
    The relationship between a category and an arbitrary object
    """
    category = models.ForeignKey(Category, related_name='items')
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    object = generic.GenericForeignKey('content_type', 'object_id')
    sort_order = models.IntegerField(default=0)

def pre_save_category(instance,**kwargs):
    if instance.parent is None:
        try:
            instance.parent = Category.objects.get_root()
        except Category.DoesNotExist:
            raise Exception, 'root node does not exist, please run syncdb'
    params = dict(
        table = connection.ops.quote_name(Category._meta.db_table),
        lookup_val = instance.parent.rgt - 1,
    )
    cursor = connection.cursor()
    cursor.execute("""
    UPDATE %(table)s SET rgt = rgt + 2 WHERE rgt > %(lookup_val)i
    """ % params)
    cursor.execute("""
    UPDATE %(table)s SET lft = lft + 2 WHERE lft > %(lookup_val)i
    """ % params)
    instance.lft = params['lookup_val'] + 1
    instance.rgt = params['lookup_val'] + 2
    
signal=signals.pre_save 
signal.connect(pre_save_category, sender=Category) 


def post_delete_category():
    pass

