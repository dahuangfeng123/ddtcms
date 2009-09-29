import datetime
from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.
class BaseCategoryAbstractModel(models.Model):
    """
    An abstract base class that any custom Category models probably should
    subclass.
    """
    name          = models.CharField(_('name'), max_length=50)
    slug          = models.SlugField(max_length=50,help_text='alias to the name,use english')
    parent        = models.ForeignKey('self',null=True,blank=True,related_name='%(model)s_category_children')
    depth         = models.PositiveSmallIntegerField(_("category's depth"), blank=True,null=True)
    order         = models.PositiveSmallIntegerField(_('order'), default=0)

    class Meta:
        abstract = True


class AbstractBaseEntryModel(models.Model):
    """
    An abstract base class that any custom Information Entry(News,Article,blog,forum post,question,etc) models probably should
    subclass.
    """
    title         = models.CharField(_('name'), max_length=50)
    slug          = models.SlugField(max_length=50,help_text='alias to the name,use english')
    parent        = models.ForeignKey('self',null=True,blank=True,related_name='%(model)s_category_children')
    depth         = models.PositiveSmallIntegerField(_("category's depth"), blank=True,null=True)
    order         = models.PositiveSmallIntegerField(_('order'), default=0)

    class Meta:
        abstract = True
        


        
class AbstractBaseDublinCoreModel(models.Model):
	"""
	An abstract base class that any custom Dublin Core Meta data models probably should
	subclass.
	"""

	contributor = models.CharField(_('contributor'), max_length=50)
	coverage    = models.CharField(_('coverage'), max_length=50)
	creator     = models.CharField(_('creator'), max_length=50)
	date        = models.DateTimeField(_('date'), max_length=50)
	description = models.CharField(_('description'), max_length=50)
	format      = models.CharField(_('format'), max_length=50)
	identifier  = models.CharField(_('identifier'), max_length=50)
	language    = models.CharField(_('language'), max_length=50)
	publisher   = models.CharField(_('publisher'), max_length=50)
	relation    = models.CharField(_('relation'), max_length=50)
	rights      = models.CharField(_('rights'), max_length=50)
	source      = models.CharField(_('source'), max_length=50)
	subject     = models.CharField(_('subject'), max_length=50)
	title       = models.CharField(_('title'), max_length=50)
	type        = models.CharField(_('type'), max_length=50)



	class Meta:
	    abstract = True	