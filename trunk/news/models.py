from django.db import models
from django.contrib.auth.models import User
from ddtcms.blog.models import Entry

# Create your models here.


class News(Entry):
    pass
    
class Meta:
    ordering = ('-pub_date',)
    get_latest_by = 'pub_date'
    
