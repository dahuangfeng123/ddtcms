from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.contrib.auth.models import User
from django.conf import settings
from django.template.defaultfilters import slugify
from django.utils import encoding
from django.utils.http import urlquote
import os
import re
from datetime import datetime
import mimetypes
from django.contrib.contenttypes.models import ContentType
from ddtcms.utils.uploadfile import randomfilename
# Get relative media path
try:
    ATTACHMENT_DIR = settings.ATTACHMENT_DIR
except:
    ATTACHMENT_DIR = "attachments"



def unique_slugify(instance, value, slug_field_name='slug', queryset=None,
                   slug_separator='-'):    
    """     
    Calculates a unique slug of ``value`` for an instance.

    ``slug_field_name`` should be a string matching the name of the field to
    store the slug in (and the field to check against for uniqueness).

    ``queryset`` usually doesn't need to be explicitly provided - it'll default
    to using the ``.all()`` queryset from the model's default manager.
    
    from http://www.djangosnippets.org/snippets/690/    
    """
    
    slug_field = instance._meta.get_field(slug_field_name)

    slug = getattr(instance, slug_field.attname)
    slug_len = slug_field.max_length

    # Sort out the initial slug. Chop its length down if we need to.
    slug = slugify(value)
    if slug_len:
        slug = slug[:slug_len]
    slug = _slug_strip(slug, slug_separator)
    original_slug = slug

    # Create a queryset, excluding the current instance.
    if not queryset:
        queryset = instance.__class__._default_manager.all()
        if instance.pk:
            queryset = queryset.exclude(pk=instance.pk)

    # Find a unique slug. If one matches, at '-2' to the end and try again
    # (then '-3', etc).
    next = 2
    while not slug or queryset.filter(**{slug_field_name: slug}):
        slug = original_slug
        end = '-%s' % next
        if slug_len and len(slug) + len(end) > slug_len:
            slug = slug[:slug_len-len(end)]
            slug = _slug_strip(slug, slug_separator)
        slug = '%s%s' % (slug, end)
        next += 1

    setattr(instance, slug_field.attname, slug)


def _slug_strip(value, separator=None):
    """
    Cleans up a slug by removing slug separator characters that occur at the
    beginning or end of a slug.

    If an alternate separator is used, it will also replace any instances of
    the default '-' separator with the new separator.
    """
    if separator == '-' or not separator:
        re_sep = '-'
    else:
        re_sep = '(?:-|%s)' % re.escape(separator)
        value = re.sub('%s+' % re_sep, separator, value)
    return re.sub(r'^%s+|%s+$' % (re_sep, re_sep), '', value)
    

class AttachmentManager(models.Manager):
    """
    Methods borrowed from django-threadedcomments
    """
    
    def _generate_object_kwarg_dict(self, content_object, **kwargs):
        """
        Generates the most comment keyword arguments for a given ``content_object``.
        """
        kwargs['content_type'] = ContentType.objects.get_for_model(content_object)
        kwargs['object_id'] = getattr(content_object, 'pk', getattr(content_object, 'id'))
        return kwargs

    def create_for_object(self, content_object, **kwargs):
        """
        A simple wrapper around ``create`` for a given ``content_object``.
        """
        return self.create(**self._generate_object_kwarg_dict(content_object, **kwargs))
        
    def attachments_for_object(self, content_object, **kwargs):
        """
        Prepopulates a QuerySet with all attachments related to the given ``content_object``.
        """
        return self.filter(**self._generate_object_kwarg_dict(content_object, **kwargs))


class Attachment(models.Model):
    file = models.FileField(upload_to=ATTACHMENT_DIR)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey("content_type", "object_id") 
    attached_timestamp = models.DateTimeField("Date attached", default=datetime.now)
    title = models.CharField(max_length=200)
    slug = models.SlugField(editable=False)
    summary = models.TextField()
    attached_by = models.ForeignKey(User, related_name="attachment_attached_by", editable=False)
    mimetype = models.CharField(editable=False, max_length=100)
    
    objects = AttachmentManager()

    class Meta:
        ordering = ['-attached_timestamp']
        get_latest_by = 'attached_timestamp'

    def __unicode__(self):
        return self.title
    
    def save(self, force_insert=False, force_update=False):
        unique_slugify(self, self.title)
        file_path = '%s%s' % (settings.MEDIA_ROOT, self.file.name)
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
            
    def get_absolute_url(self):
		return '%supload/attachement/%s' % (settings.MEDIA_URL, self.file.url)
    
    def save_uploaded_file(self,memoryfiledfile):
            file_path =os.path.join(ATTACHMENT_DIR, randomfilename(memoryfiledfile.name))
            self.file.save(file_path, memoryfiledfile)            
            #destination = open(file_path, 'wb+')
            #for chunk in memoryfiledfile.chunks():
            #    destination.write(chunk)
            
#    def handle_uploaded_attachment(self,model_object,attachment_file,attached_by,title=None,summary=None):
#        if title is None:
#            title = attachment_file.name
#        if summary is None:
#            summary = attachment_file.name
#        object_type = ContentType.objects.get_for_model(model_object)
#        object_id   = model_object.id
#        attach=Attachment(
#            content_type = object_type,
#            object_id    = object_id,
#            title        = title,
#            summary      = summary,
#            attached_by  = attached_by
#            )
#        attach.save_uploaded_file(attachment_file)
#        attach.save()

    def handle_uploaded_attachment(self,model_object,attachment_file,attached_by,title=None,summary=None):
        if title is None:
            title = attachment_file.name
        if summary is None:
            summary = attachment_file.name
        object_type = ContentType.objects.get_for_model(model_object)
        object_id   = model_object.id
        
        self.content_type = object_type
        self.object_id    = object_id
        self.title        = title
        self.summary      = summary
        self.attached_by  = attached_by
        self.mimetype     = attachment_file.content_type
        
        file_path =os.path.join(ATTACHMENT_DIR, randomfilename(attachment_file.name))
        self.file.save(file_path, attachment_file,save=False)
        self.save()
            
class TestModel(models.Model):
    """
    This model is simply used by this application's test suite as a model to 
    which to attach files.
    """
    name = models.CharField(max_length=32)
    date = models.DateTimeField(default=datetime.now)
