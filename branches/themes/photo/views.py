#coding=utf-8
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import Context, loader
from ddtcms.photo.models import Photo
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from StringIO import StringIO
import PIL
import datetime

from django.template import RequestContext
from ddtcms.photo.forms import UploadPhotoForm
from ddtcms.utils.uploadfile import genfilename,handle_uploaded_file


def upload(request):
    if request.method == 'POST': # If the form has been submitted...
        form = UploadPhotoForm(data=request.POST, files=request.FILES) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            fname,dname=handle_uploaded_file(request.FILES['pic'])
            photo=Photo(topic=request.POST['topic'],pic= fname, user=request.user,pub_date=datetime.datetime.now())
            photo.save()
            return HttpResponseRedirect('/'+fname) # Redirect after POST

    else:
        form = UploadPhotoForm() # An unbound form

    return render_to_response('photo/photo_upload.html',
            {'form': form, },
            context_instance=RequestContext(request))




