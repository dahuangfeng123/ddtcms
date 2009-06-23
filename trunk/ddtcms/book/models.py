from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Publisher(models.Model):
     name = models.CharField(max_length=30)
     address = models.CharField(max_length=50)
     city = models.CharField(max_length=60)
     state_province = models.CharField(max_length=30)
     country = models.CharField(max_length=50)
     website = models.URLField()
     
     class Meta:
     	verbose_name = _('Publisher')
        verbose_name_plural = _('Publishers')

class Author(models.Model):
     salutation = models.CharField(max_length=10)
     first_name = models.CharField(max_length=30)
     last_name = models.CharField(max_length=40)
     email = models.EmailField()
     headshot = models.ImageField(upload_to='/face/')
     
     class Meta:
     	verbose_name = _('Book Author')
        verbose_name_plural = _('Book Authors')

class Book(models.Model):
     title = models.CharField(max_length=100)
     authors = models.ManyToManyField(Author)
     publisher = models.ForeignKey(Publisher)
     publication_date = models.DateField()
     cover = models.ImageField(upload_to='/book/cover/')
     class Meta:
     	verbose_name = _('Book')
        verbose_name_plural = _('Books')
     
class Chapter(models.Model):
    title=models.CharField(max_length=200)
    book=models.ForeignKey(Book)
    content=models.TextField()
    
    class Meta:
     	verbose_name = _('Book Chapter')
        verbose_name_plural = _('Book Chapters')
    