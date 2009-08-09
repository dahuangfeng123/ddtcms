from django.db import models
from photologue.models import Gallery, Photo
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.contrib.auth.models import User
from django.conf import settings
from django.template.defaultfilters import slugify
from django.utils import encoding
from django.utils.http import urlquote

import re
from datetime import datetime
import mimetypes

# Create your models here.
class Special(models.Model):
    
    content_type   = models.ForeignKey(ContentType)
    object_id      = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey("content_type", "object_id") 
    title          = models.CharField(max_length=100)
    slug           = models.SlugField()
    description    = models.TextField()
    photo          = models.ForeignKey(Photo, null=True, blank=True)
    pub_date       = models.DateTimeField("Date added", default=datetime.now)
    
    #objects = SpecialManager()

    class Meta:
        ordering = ['-pub_date']
        get_latest_by = 'pub_date'

    def __unicode__(self):
        return self.title
    
    def save(self, force_insert=False, force_update=False):
        unique_slugify(self, self.title)
        file_path = '%s%s' % (settings.MEDIA_ROOT, self.file)
        (mime_type, encoding) = mimetypes.guess_type(file_path)
        try:
            self.mimetype = mime_type
        except:
            self.mimetype = 'text/plain'
        super(Attachment, self).save(force_insert, force_update)
        
        
    def file_url(self):
        return encoding.iri_to_uri(self.file.url)
    
    def mime_type(self):
        return '%s' % self.mimetype
    
    def type_slug(self):
        return slugify(self.mimetype.split('/')[-1])
    
    def is_image(self):
    	file_type=self.mimetype.split('/')[0]
        if file_type == 'image':
            return True
        else:
            return False