from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from ddtcms.member.countries import COUNTRIES
from ddtcms.member.countries import CountryField
from django.template.defaultfilters import slugify




        
        

# Create your models here.
class Organization(models.Model):
	"""
	An abstract base class that any custom Category models probably should
	subclass.
	"""
	name          = models.CharField(_('name'), max_length=50)
	slug          = models.SlugField(max_length=50,help_text='alias to the name,use english')
	parent        = models.ForeignKey('self',null=True,blank=True,related_name='Sub_Organizations')
	chief         = models.CharField(_('chief'),blank=True,null=True,max_length=50)
	description   = models.CharField(_('description'),blank=True,null=True,max_length=50)
	url           = models.URLField(_('homepage'),blank=True,null=True,verify_exists=False)
	order         = models.PositiveSmallIntegerField(_('order'), default=0)

	class Meta:
		ordering      = ('order',)
		verbose_name = _('Organization')
		verbose_name_plural = _('Organizations')
		
	def __unicode__(self):
		return self.name
		
	def get_absolute_url(self):
		if not self.url:
			self.url="http://"
		return self.url
		
	def save(self,*args,**kwargs):
		if not self.slug:
			self.slug = slugify(self.name)
			self.slug = self.slug.lower().replace('-','_')
		super(Organization,self).save(*args,**kwargs)



	
			
class Person(models.Model):
	user = models.ForeignKey(User, blank=True, null=True, related_name="real_person")
	family_name  = models.CharField(max_length=40,blank=True, null=True)
	given_name   = models.CharField(max_length=40)
	country      = CountryField(null=True, blank=True,default="CN")
	organization = models.ForeignKey(Organization, blank=True, null=True, related_name="org_members")
	slug         = models.SlugField(blank=True, null=True)
	

	
	class Meta:
		ordering     = ('slug','given_name',)
		verbose_name = _('Person')
		verbose_name_plural = _('Persons')
		
	def __unicode__(self):
		return self.fullname()
			
	def get_absolute_url(self):
		return "/people/%d/" % (self.id)
		
	def save(self,*args,**kwargs):
		if not self.slug:
			self.slug = slugify(self.given_name)
			self.slug = self.slug.lower().replace('-','_')
		super(Person,self).save(*args,**kwargs)
		
	def fullname(self):
		if self.is_easterner():
			return "%s%s" % (self.family_name,self.given_name)
		else:
			return "%s %s" % (self.given_name,self.family_name)
	
	def is_easterner(self):
		return self.country in ("CN","HK","TW","JP","KR","KP","SG")

		




class Contact(models.Model):
	person           = models.ForeignKey(Person)
	mobile           = models.CharField(max_length=40,null=True,blank=True)
	phone            = models.CharField(max_length=40,null=True,blank=True)
	address          = models.CharField(max_length=40,null=True,blank=True)
	state            = models.CharField(max_length=40,null=True,blank=True)
	postal           = models.CharField(max_length=40,null=True,blank=True)
	country          = models.CharField(max_length=40,null=True,blank=True)
	msn              = models.CharField(max_length=40,null=True,blank=True)
	webpage          = models.CharField(max_length=40,null=True,blank=True)
	city             = models.CharField(max_length=40,null=True,blank=True)
	icq              = models.CharField(max_length=40,null=True,blank=True)
	company          = models.CharField(max_length=40,null=True,blank=True)
	jobtitle         = models.CharField(max_length=40,null=True,blank=True)
	businessfax      = models.CharField(max_length=40,null=True,blank=True)
	businessphone    = models.CharField(max_length=40,null=True,blank=True)
	birthday         = models.CharField(max_length=40,null=True,blank=True)
	email            = models.CharField(max_length=40,null=True,blank=True)
	businessemail    = models.CharField(max_length=40,null=True,blank=True)
	businesswebpage  = models.CharField(max_length=40,null=True,blank=True)
	businessaddress  = models.CharField(max_length=40,null=True,blank=True)
	businesscity     = models.CharField(max_length=40,null=True,blank=True)
	businessstate    = models.CharField(max_length=40,null=True,blank=True)
	businesspostal   = models.CharField(max_length=40,null=True,blank=True)
	businesscountry  = models.CharField(max_length=40,null=True,blank=True)
	businessmobile   = models.CharField(max_length=40,null=True,blank=True)
	photo            = models.CharField(max_length=40,null=True,blank=True)
	notes            = models.CharField(max_length=40,null=True,blank=True)

	class Meta:
		ordering     = ('person',)
		verbose_name = _('Contact')
		verbose_name_plural = _('Contacts')
		
	def __unicode__(self):
		return self.person.fullname()

	def get_absolute_url(self):
		return "/pelple/%s/" % (self.person.fullname())
		



		
class Friend(models.Model):
	person           = models.ForeignKey(Person)
	friend           = models.CharField(max_length=40,null=True,blank=True)
	nickname         = models.CharField(max_length=40,null=True,blank=True)
	notes            = models.CharField(max_length=40,null=True,blank=True)

	class Meta:
		ordering     = ('person',)
		verbose_name = _('Friend')
		verbose_name_plural = _('Friends')
		
	def __unicode__(self):
		return self.person.fullname()

	def get_absolute_url(self):
		return "/pelple/%s/" % (self.person.fullname())