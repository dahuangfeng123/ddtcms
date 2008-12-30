from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from ddtcms.category.models import Category
import datetime
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
class Entry(models.Model):
    title         = models.CharField(max_length=200)
    pub_date      = models.DateTimeField('date published',blank=True,default=datetime.datetime.now)
    content       = models.TextField()
    user          = models.ForeignKey(User,verbose_name='Author', editable=False)
    category      = models.ForeignKey(Category,null=True)
    slug          = models.SlugField(
                  unique_for_date='pub_date',
                  help_text='Automatically built From the title.'
                  )
    summary       = models.TextField(help_text="One paragraph. Don't add tag.")
    tags          = TagField(help_text=tagfield_help_text, verbose_name=_('tags'))



    class Meta:
        ordering      = ('-pub_date',)
#        get_latest_by = 'pub_date'
#        db_table      = "blog_entry"


    def get_absolute_url(self):
        return "/blog/%s/%s/" % (self.pub_date.strftime("%Y/%b/%d").lower(), self.slug)

    def __unicode__(self):
        return self.title
        
