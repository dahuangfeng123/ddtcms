from django.db import models
from django.contrib.auth.models import User 
from ddtcms  import settings



import datetime
# Create your models here.
class Photo(models.Model):


    topic         = models.CharField(blank=True,null=True,max_length=64)
    pub_date      = models.DateTimeField('date published',null=True,default=datetime.datetime.now())    
    user          = models.ForeignKey(User)
    pic           = models.ImageField(upload_to='upload/photo/%Y/%m/%d',blank=True,null=True)
    
    def __unicode__(self):
        return self.topic

    def get_absolute_url(self):
        return self.pic.url