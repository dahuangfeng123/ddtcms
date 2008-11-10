from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Profile(models.Model):
    user          = models.ForeignKey(User, unique=True, verbose_name=_('user'))
    nickname      = models.CharField(max_length=20)
    foreigname    = models.CharField(max_length=20)
    birthday      = models.DateField('birthday')
    sex           = models.CharField(max_length=2)
    bloodgroup    = models.CharField(max_length=4)
    height        = models.CharField(max_length=4)
    weight        = models.CharField(max_length=4)
    nation        = models.CharField(max_length=10)
    homeplace     = models.CharField(max_length=20)
    hobby         = models.CharField(max_length=20)
    character     = models.CharField(max_length=20)
    profession    = models.CharField(max_length=20)
    strongsuit    = models.CharField(max_length=40)
    occupation    = models.CharField(max_length=20)
    intro         = models.TextField(max_length=200)
    public_profile_field=models.BooleanField(default=True)
    
    def __unicode__(self):
        return self.user.username
    
    def get_absolute_url(self):
        return "/member/%s/profile" % (self.user.username)
        
        
        
        
class Resume(models.Model):
    user          = models.ForeignKey(User, unique=True, verbose_name=_('user'))
    startime      = models.DateField()
    stoptime      = models.DateField()
    event         = models.TextField(max_length=200)
    
    def __unicode__(self):
        return self.user.username
    
    def get_absolute_url(self):
        return "/member/%s/resume" % (self.user.username)



class Favourite(models.Model):
    user          = models.ForeignKey(User, unique=True, verbose_name=_('user'))
    moviestar     = models.CharField(max_length=40)
    movie         = models.CharField(max_length=40)
    sport         = models.CharField(max_length=40)
    singer        = models.CharField(max_length=40)
    song          = models.CharField(max_length=40)
    language      = models.CharField(max_length=40)
    cartoon       = models.CharField(max_length=40)
    clothing      = models.CharField(max_length=40)
    colour        = models.CharField(max_length=40)
    writer        = models.CharField(max_length=40)
    book          = models.CharField(max_length=200)
    season        = models.CharField(max_length=40)
    food          = models.CharField(max_length=40)
    drink         = models.CharField(max_length=40)
    relaxation    = models.CharField(max_length=40)
    recreation    = models.CharField(max_length=40)    
  
    
    def __unicode__(self):
        return self.user.username
    
    def get_absolute_url(self):
        return "/member/%s/favourite" % (self.user.username)
