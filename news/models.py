import datetime
from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.comments.models import Comment
from django.template.defaultfilters import slugify
from attachments.models import Attachment
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
from news.managers import CategoryManager
from news.managers import NewsManager


class Category(models.Model):
	name          = models.CharField(_('name'), max_length=50)
	slug          = models.SlugField(max_length=50,unique=True,help_text='alias to the name,use english')
	parent        = models.ForeignKey('self',null=True,blank=True,related_name='child')
	depth         = models.PositiveSmallIntegerField(_("category's depth"), blank=True,null=True)
	path          = models.CharField(_("category's path"),blank=True,null=True, max_length=250, editable=False)
	posts         = models.IntegerField(_("News Posts Count"), default=0)
	order         = models.PositiveSmallIntegerField(_('order'), default=0)
	
	objects       = CategoryManager()
	

	class Meta:
		ordering            =  ('parent__id','order','slug',)
		verbose_name        = _('News Category')
		verbose_name_plural = _('News Categories')  
	
	def __unicode__(self):
		return self.name    
	
	def save(self,*args,**kwargs):
		if not self.slug:
			self.slug = slugify(self.title)
			self.slug = self.slug.lower().replace('-','_')

		super(Category,self).save(*args,**kwargs)
		if not self.path:
			p_list = self._recurse_for_parents_id(self)
			p_list.append(self.id)
			#self.path = '%s' % '/'.join (p_list)
			#self.path = '/'.join (p_list)
			self.depth = len(p_list)
			self.path = '/'.join(map(str, p_list))
			self.save()
		if not self.depth:
			p_list = self.path.split('/')
			self.depth = len(p_list)
			self.save()


	
	def is_root(self):
		if self.parent == None:
			return True
		return False
	
	def get_root(self):
		p = self.parent
		if p:
			p=p.get_root()
		else:
			p=self
		return p
		
	def get_depth(self):
		if not self.depth:
			p_list = self.path.split('/')
			self.depth = len(p_list)
			self.save()
		return self.depth

	def _recurse_for_parents_id(self, category_obj):
		#This is used for the urls
		p_list = []
		if category_obj.parent_id:
			p = category_obj.parent
			p_list.append(p.id)
			more = self._recurse_for_parents_id(p)
			p_list.extend(more)
		if category_obj == self and p_list:
			p_list.reverse()
		return p_list

	def _recurse_for_parents_slug(self, category_obj):
		#This is used for the urls
		p_list = []
		if category_obj.parent_id:
			p = category_obj.parent
			p_list.append(p.slug)
			more = self._recurse_for_parents_slug(p)
			p_list.extend(more)
		if category_obj == self and p_list:
			p_list.reverse()
		return p_list
			
	#def get_absolute_url(self):
	#   return "/news/category/%s/" %  self.slug
	def get_absolute_url(self):
		p_list = self._recurse_for_parents_slug(self)
		p_list.append(self.slug)
		return '%s%s/' % (reverse('news-index'), '/'.join (p_list))
		
	def _recurse_for_parents_name_url(self, category__obj):
		#Get all the absolute urls and names (for use in site navigation)
		p_list = []
		url_list = []
		if category__obj.parent_id:
			p = category__obj.parent
			p_list.append(p.name)
			url_list.append(p.get_absolute_url())
			more, url = self._recurse_for_parents_name_url(p)
			p_list.extend(more)
			url_list.extend(url)
		if category__obj == self and p_list:
			p_list.reverse()
			url_list.reverse()
		return p_list, url_list

	def get_url_name(self):
		#Get a list of the url to display and the actual urls
		p_list, url_list = self._recurse_for_parents_name_url(self)
		p_list.append(self.name)
		url_list.append(self.get_absolute_url())
		return zip(p_list, url_list)

	def _flatten(self, L):
		"""
		Taken from a python newsgroup post
		"""
		if type(L) != type([]): return [L]
		if L == []: return L
		return self._flatten(L[0]) + self._flatten(L[1:])
	
	def _recurse_for_children(self, node):
		children = []
		children.append(node)
		for child in node.child.all():
			children_list = self._recurse_for_children(child)
			children.append(children_list)
		return children

	def get_all_children(self):
		"""
		Gets a list of all of the children forums.
		"""
		children_list = self._recurse_for_children(self)
		flat_list = self._flatten(children_list[1:])
		return flat_list
	
	def get_children(self):
		return self.child.all()
	
	def has_children(self):
		if self.get_children():
			return True
		else:
			return False
		
	def total_posts(self):
		total=0
		if not self.get_children():
			total = self.posts
		else:
			for c in self.get_all_children():
				total += c.posts
		return total

		

NEWS_STATUS = (
(0,  _('UNAPPROVED')),
(1,  _('APPROVED')),
(2,  _('HEADLINE')),
(3,  _('RECOMMENDED')),
(4,  _('FLASHSLIDE')),
(9,  _('DELETED')),
)



class News(models.Model):
	title         = models.CharField(max_length=100)
	subtitle      = models.CharField(max_length=100,null=True,blank=True)
	slug          = models.SlugField(blank=True,unique=True,help_text='Automatically built From the title.')
	deliverer     = models.ForeignKey(User,verbose_name='Deliverer',null=True,editable=True)
	category      = models.ForeignKey(Category,null=True)
	pub_date      = models.DateTimeField('date published',blank=True,default=datetime.datetime.now)
	content       = models.TextField()
	summary       = models.TextField(help_text="Summary",null=True,blank=True)
	tags          = TagField(help_text=tagfield_help_text, verbose_name=_('tags'))
	source        = models.CharField(verbose_name='News Source',max_length=50,null=True,blank=True,help_text='Where the news comes from')
	views         = models.PositiveIntegerField(_("Views"), default=0)
	comments      = models.PositiveIntegerField(_("Comments"), default=0)
	allow_comments = models.BooleanField(_("Allow Comments"),default=True)
	pic           = models.CharField('News Indicator Pic',max_length=200,null=True,blank=True,help_text="If has a pic url,show on homepage or indexpage")
	status        = models.PositiveIntegerField(_("Status"), choices=NEWS_STATUS, default=0)
	#SmallIntegerField
	editor        = models.CharField(max_length=20,blank=True)
	
	objects = NewsManager()
	
	class Meta:
		ordering      = ('-pub_date',)
		unique_together = (('slug', 'pub_date'), )
		get_latest_by = 'pub_date'
		verbose_name = _('News')
		verbose_name_plural = _('News')
	
	def get_absolute_url(self): 
		if self.slug=="":
			return "/news/%s/%s/" % (self.pub_date.strftime("%Y/%b/%d").lower(), self.id)
		else:
			return "/news/%s/%s/" % (self.pub_date.strftime("%Y/%b/%d").lower(), self.slug)
	
	def __unicode__(self):
		return self.title
	
	def get_previous(self):
		try:
			# isnull is to check whether it's published or not - drafts don't have dates, apparently
			return News.objects.all().filter(pub_date__lt=self.pub_date,pub_date__isnull=False)[0]
		except IndexError, e:
			# print 'Exception: %s' % e.message
			return None
			
	def get_next(self):
		try:
			# isnull is to check whether it's published or not - drafts don't have dates, apparently
			return News.objects.all().filter(pub_date__gt=self.pub_date,pub_date__isnull=False).order_by('pub_date')[0]
		except IndexError, e:
			# print 'Exception: %s' % e.message
			return None
			
	def approved_comments(self):
		return Comment.objects.for_model(self).filter(is_public=True)
		
	def unapproved_comments(self):
		return Comment.objects.for_model(self).filter(is_public=False)
		
	def total_comments(self):
		return Comment.objects.for_model(self)   
	
	def total_attachments(self):
		return Attachment.objects.attachments_for_object(self) 
	
	def today_posts(self):
		ps = []
		return 0
	
	def is_pic(self):		
		return (not self.pic=="")

	def save(self,*args,**kwargs):
		if not self.slug:
			self.slug = slugify(self.title)
			self.slug = self.slug.lower().replace('-','_')
			print 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
		super(News,self).save(*args,**kwargs)
		
		c = self.category
		c.posts = c.news_set.count()
		c.save()


		
	#def send_latest_to_notice(self,title,pub_date,over_date,content,slug):
	#	latest_news_added.send(sender=self, title=title,pub_date=pub_date,over_date=over_date,content=content,slug=slug)




