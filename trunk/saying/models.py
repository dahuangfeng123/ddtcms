from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from ddtcms.people.models import Person
# Create your models here.
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


class Saying(models.Model):
	title         = models.CharField(max_length=200,null=True,default="")
	said_date     = models.DateTimeField('date said',null=True,default="")
	sayer         = models.ForeignKey(Person,verbose_name='Sayer',null=True,editable=True)
	content       = models.TextField()
	background    = models.TextField(null=True,default="")
	source        = models.CharField(max_length=200,null=True,default="")
	slug          = models.SlugField(max_length=50)
	deliverer     = models.ForeignKey(User,verbose_name='Deliverer',null=True,editable=True)
	pub_date      = models.DateTimeField('date published')
	tags          = TagField(help_text=tagfield_help_text, verbose_name=_('tags'))
	
	views         = models.PositiveIntegerField(_("Views"), default=0)
	comments      = models.PositiveIntegerField(_("Comments"), default=0)
	likes         = models.PositiveIntegerField(_("Likes"), default=0)
	dislikes      = models.PositiveIntegerField(_("Dislikes"), default=0)
	collects      = models.PositiveIntegerField(_("Collects"), default=0)
	discloses     = models.PositiveIntegerField(_("Discloses"), default=0)
	
	class Meta:
		ordering      = ('-pub_date',)
		verbose_name = _('Saying')
		verbose_name_plural = _('Sayings')

	def __unicode__(self):
		return self.title
	
	def get_absolute_url(self):
		return "/saying/%s/" % (self.slug)