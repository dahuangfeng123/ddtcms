from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from ddtcms.blog.models import Entry

# Create your models here.


class Article(Entry):
    pass
    
    class Meta:
        ordering = ('-pub_date',)
        get_latest_by = 'pub_date'
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')
    
