from django.db import models

# Create your models here.
class Notice(models.Model):
    title         = models.CharField(max_length=200)
    pub_date      = models.DateTimeField('date published')
    content       = models.TextField()
    slug          = models.SlugField(max_length=50)
    
    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        return "/notice/%s/" % (self.slug)