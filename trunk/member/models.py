# coding=UTF-8
from django.db import models
from django.contrib.auth.models import User
from userprofile.models import BaseProfile
from django.utils.translation import ugettext as _
from django.conf import settings
import datetime



GENDER_CHOICES = ( ('F', _('Female')), ('M', _('Male')),)
BLOODGROUP_CHOICES= ( ('A',  _('A TYPE')),
                      ('B',  _('B TYPE')),
                      ('AB', _('AB TYPE')),
                      ('O',  _('O TYPE')),
                      ('R',  _('OTHER TYPE')),)

ZODIAC_CHOICES=(
('RAT',      _('Rat')),
('OX',       _('Ox')),
('TIGER',    _('Tiger')),
('RABBIT',   _('Rabbit')),
('DRAGON',   _('Dragon')),
('SNAKE',    _('Snake')),
('HORSE',    _('Horse')),
('GOAT',     _('Goat')),
('MONKEY',   _('Monkey')),
('ROOSTER',  _('Rooster')),
('DOG',      _('Dog')),
('PIG',      _('Pig')),
)

CONSTELLATION_CHOICES=(
('ARIES',       _('Aries(the Ram)')),
('TAURUS',      _('Taurus(the Bull)')),
('GEMINI',      _('Gemini(the Twins)')),
('CANCER',      _('Cancer(the Crab)')),
('LEO',         _('Leo(the Lion)')),
('VIRGO',       _('Virgo(the Virgin)')),
('LIBRA',       _('Libra(the Scales)')),
('SCORPIO',     _('Scorpio(the Scorpion)')),
('SAGITTALIUS', _('Sagittarius(the Archer)')),
('CAPRICORNUS', _('Capricornus(the Goat)')),
('AQUALIUS',    _('Aquarius(the Water Carrier)')),
('PISCES',      _('Pisces(the Fishes)')),
)

# Create your models here.
class Profile(BaseProfile):

    firstname      = models.CharField(max_length=255, blank=True)
    surname        = models.CharField(max_length=255, blank=True)
    nickname       = models.CharField(null=True,max_length=20)
    foreigname     = models.CharField(null=True,max_length=20)
    birthday       = models.DateField(null=True,verbose_name=_('birthday'),default=datetime.date.today(), blank=True)
    gender         = models.CharField(null=True,max_length=1, choices=GENDER_CHOICES, blank=True)
    bloodgroup     = models.CharField(null=True,max_length=4, choices=BLOODGROUP_CHOICES,blank=True)
    zodiac         = models.CharField(null=True,max_length=20, choices=ZODIAC_CHOICES,blank=True)
    constellation  = models.CharField(null=True,max_length=20, choices=CONSTELLATION_CHOICES,blank=True)
    height         = models.CharField(null=True,max_length=4)
    weight         = models.CharField(null=True,max_length=4)
    homeplace      = models.CharField(null=True,max_length=20)
    hobby          = models.CharField(null=True,max_length=20)
    character      = models.CharField(null=True,max_length=20)
    profession     = models.CharField(null=True,max_length=20)
    career         = models.CharField(null=True,max_length=20)
    skills         = models.CharField(null=True,max_length=40)    
    webpage        = models.URLField(null=True,blank=True)
    intro          = models.TextField(null=True,max_length=200)
    is_public      = models.BooleanField(default=True)

    def __unicode__(self):
        return self.user.username

    #def get_absolute_url(self):
    #    return "/member/%s/profile" % (self.user.username)




class Resume(models.Model):
    user          = models.ForeignKey(User, unique=True, verbose_name=_('user'))
    startime      = models.DateField()
    stoptime      = models.DateField()
    event         = models.TextField(max_length=200)

    def __unicode__(self):
        return self.user.username

    def get_absolute_url(self):
        return "/member/%s/resume" % (self.user.username)

#class Education(models.Model):
#    user          = models.ForeignKey(User, unique=True, verbose_name=_('user'))
#    degree        = models.CharField(null=True,max_length=20)
#    school        = models.CharField(null=True,max_length=20)
#    notes         = models.TextField(max_length=200)
#
#    def __unicode__(self):
#        return self.user.username
#
#    def get_absolute_url(self):
#        return "/member/%s/resume" % (self.user.username)


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

#class contact:
#    lastname         = models.CharField(max_length=40,null=True)
#    firstname        = models.CharField(max_length=40,null=True)
#    mobile           = models.CharField(max_length=40,null=True)
#    phone            = models.CharField(max_length=40,null=True)
#    address          = models.CharField(max_length=40,null=True)
#    state            = models.CharField(max_length=40,null=True)
#    postal           = models.CharField(max_length=40,null=True)
#    country          = models.CharField(max_length=40,null=True)
#    msn              = models.CharField(max_length=40,null=True)
#    webpage          = models.CharField(max_length=40,null=True)
#    city             = models.CharField(max_length=40,null=True)
#    icq              = models.CharField(max_length=40,null=True)
#    company          = models.CharField(max_length=40,null=True)
#    jobtitle         = models.CharField(max_length=40,null=True)
#    businessfax      = models.CharField(max_length=40,null=True)
#    businessphone    = models.CharField(max_length=40,null=True)
#    birthday         = models.CharField(max_length=40,null=True)
#    email            = models.CharField(max_length=40,null=True)
#    businessemail    = models.CharField(max_length=40,null=True)
#    businesswebpage  = models.CharField(max_length=40,null=True)
#    businessaddress  = models.CharField(max_length=40,null=True)
#    businesscity     = models.CharField(max_length=40,null=True)
#    businessstate    = models.CharField(max_length=40,null=True)
#    businesspostal   = models.CharField(max_length=40,null=True)
#    businesscountry  = models.CharField(max_length=40,null=True)
#    businessmobile   = models.CharField(max_length=40,null=True)
#    photo            = models.CharField(max_length=40,null=True)
#    notes            = models.CharField(max_length=40,null=True)
#
#    def __unicode__(self):
#        return self.user.username
#
#    def get_absolute_url(self):
#        return "/member/%s/favourite" % (self.user.username)