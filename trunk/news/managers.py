import datetime
from django.db import models
from django.db.models import Q


class CategoryManager(models.Manager):
	def get_all_roots(self):
		return self.filter(parent__isnull = True)


class NewsManager(models.Manager):
	def get_published(self):
		return self.filter(status__gt=0, pub_date__lte=datetime.datetime.now)
	def get_privated(self):
		return self.filter(status__exact=0)
	def get_headlines(self):
		return self.filter(status__exact=2)
	def get_recommended(self):
		return self.filter(status__exact=3)		
	def get_flashslide(self):
		return self.filter(status__exact=4)
	
	def for_category(self,category):
		return self.filter(category=category)
	def for_categories(self,category):
		categories=category.get_all_children()
		categories.append(category)
		return self.filter(category__in=categories)
