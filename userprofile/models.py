# coding=UTF-8
from django.db import models
from django.contrib.sites.models import Site
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext as _
from django.template import loader, Context
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.conf import settings
from userprofile.countries import CountryField
import datetime
import cPickle as pickle
import base64
import os.path
try:
    from PIL import Image, ImageFilter
except ImportError:
    import Image, ImageFilter

AVATAR_SIZES = (128, 96, 64, 48, 32, 24, 16)

class BaseProfile(models.Model):
    """
    User profile model
    """

    user = models.ForeignKey(User, unique=True)
    date = models.DateTimeField(default=datetime.datetime.now)
    country = CountryField(null=True, blank=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True)

    class Meta:
        abstract = True

    def has_avatar(self):
        return Avatar.objects.filter(user=self.user, valid=True).count()

    def __unicode__(self):
        return _("%s's profile") % self.user

    def get_absolute_url(self):
        return reverse("profile_public", args=[self.user])


class Avatar(models.Model):
    """
    Avatar model
    """
    image = models.ImageField(upload_to="userprofile/avatars/%Y/%b/%d")
    user = models.ForeignKey(User)
    date = models.DateTimeField(auto_now_add=True)
    valid = models.BooleanField()

    class Meta:
        unique_together = (('user', 'valid'),)

    def __unicode__(self):
        return _("%s's Avatar") % self.user

    def delete(self):
        base, filename = os.path.split(self.image.path)
        name, extension = os.path.splitext(filename)
        for key in AVATAR_SIZES:
            try:
                os.remove(os.path.join(base, "%s.%s%s" % (name, key, extension)))
            except:
                pass

        super(Avatar, self).delete()

    def save(self):
        for avatar in Avatar.objects.filter(user=self.user, valid=self.valid).exclude(id=self.id):
            base, filename = os.path.split(avatar.image.path)
            name, extension = os.path.splitext(filename)
            for key in AVATAR_SIZES:
                try:
                    os.remove(os.path.join(base, "%s.%s%s" % (name, key, extension)))
                except:
                    pass
            avatar.delete()

        super(Avatar, self).save()


class EmailValidationManager(models.Manager):
    """
    Email validation manager
    """
    def verify(self, key):
        try:
            verify = self.get(key=key)
            if not verify.is_expired():
                verify.user.email = verify.email
                verify.user.save()
                verify.delete()
                return True
            else:
                verify.delete()
                return False
        except:
            return False

    def getuser(self, key):
        try:
            return self.get(key=key).user
        except:
            return False

    def add(self, user, email):
        """
        Add a new validation process entry
        """
        while True:
            key = User.objects.make_random_password(70)
            try:
                EmailValidation.objects.get(key=key)
            except EmailValidation.DoesNotExist:
                self.key = key
                break
        if settings.SEND_REGISTER_MAIL:
            template_body = "userprofile/email/validation.txt"
            template_subject = "userprofile/email/validation_subject.txt"
            site_name, domain = Site.objects.get_current().name, Site.objects.get_current().domain
            body = loader.get_template(template_body).render(Context(locals()))
            subject = loader.get_template(template_subject).render(Context(locals())).strip()
            send_mail(subject=subject, message=body, from_email=None, recipient_list=[email])
        user = User.objects.get(username=str(user))
        self.filter(user=user).delete()
        return self.create(user=user, key=key, email=email)

class EmailValidation(models.Model):
    """
    Email Validation model
    """
    user = models.ForeignKey(User, unique=True)
    email = models.EmailField(blank=True)
    key = models.CharField(max_length=70, unique=True, db_index=True)
    created = models.DateTimeField(auto_now_add=True)
    objects = EmailValidationManager()

    def __unicode__(self):
        return _("Email validation process for %(user)s") % { 'user': self.user }

    def is_expired(self):
        return (datetime.datetime.today() - self.created).days > 0

    def resend(self):
        """
        Resend validation email
        """
        if settings.SEND_REGISTER_MAIL:
            template_body = "userprofile/email/validation.txt"
            template_subject = "userprofile/email/validation_subject.txt"
            site_name, domain = Site.objects.get_current().name, Site.objects.get_current().domain
            key = self.key
            body = loader.get_template(template_body).render(Context(locals()))
            subject = loader.get_template(template_subject).render(Context(locals())).strip()
            send_mail(subject=subject, message=body, from_email=None, recipient_list=[self.email])
        self.created = datetime.datetime.now()
        self.save()
        return True

class UserProfileMediaNotFound(Exception):
    pass


# add by huaitwooos@gmail.com
GENDER_CHOICES = ( ('F', _('Female')), ('M', _('Male')),)
BLOODGROUP_CHOICES= (
    ('A',  _('A TYPE')),
    ('B',  _('B TYPE')),
    ('AB', _('AB TYPE')),
    ('O',  _('O TYPE')),
    ('R',  _('OTHER TYPE')),
    )

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

#class Contact:
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
