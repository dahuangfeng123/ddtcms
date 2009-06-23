from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from ddtcms.photo.models import Photo

class UploadPhotoForm(forms.Form):

    topic = forms.CharField()
    pic   = forms.FileField()
