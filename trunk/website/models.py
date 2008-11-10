from django.db import models

# Create your models here.

class Website(models.Model):
    name          = models.CharField(max_length=200)
    domain        = models.CharField(max_length=255)
    url           = models.URLField(max_length=255)
    content       = models.TextField()
    pub_date      = models.DateTimeField('date added')
    
    
    
    def __unicode__(self):
        return self.name
    
    def get_absolute_url(self):
        return self.url