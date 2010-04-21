from django import forms
from django.utils.translation import ugettext as _
from django.forms import TextInput, Textarea
from django.conf import settings
from django.utils.safestring import mark_safe
from os.path import join
from django.template import RequestContext
from django.template.loader import render_to_string
from attachments.forms import DynamicMultipleFileField

class NicEditor(Textarea):

    class Media:
        js = ("%seditor/nicEdit/nicEdit.js" % settings.MEDIA_URL,)

    def __init__(self,  attrs=None):
    	
        self.attrs = {'class': 'niceditor','cols':50}
        if attrs:
            self.attrs.update(attrs)
            #a=self.attrs
    	#debug()
        super(NicEditor, self).__init__(self.attrs)

    def render(self, name, value, attrs=None):
        rendered = super(NicEditor, self).render(name, value, attrs)
        context = {
            'name': name,
            'MEDIA_URL':settings.MEDIA_URL,
        }
        return rendered  + mark_safe(render_to_string(
            'niceditor/niceditor.html', context))


class CreateThreadForm(forms.Form):
    title = forms.CharField(label=_("Title"),  widget=forms.TextInput(attrs={'size': 50,'class': 'required'}),	max_length=100,help_text="max_length is 100")
    body = forms.CharField(label=_("Body"), widget=NicEditor(attrs={'rows':8, 'cols':120}))
    file =  forms.FileField(label=_("Files"),widget=DynamicMultipleFileField(), required=False)
    subscribe = forms.BooleanField(label=_("Subscribe via email"), required=False)



class ReplyForm(forms.Form):
    body = forms.CharField(label=_("Body"), widget=NicEditor(attrs={'rows':8, 'cols':120}))
    file =  forms.FileField(label=_("Files"),widget=DynamicMultipleFileField(),required=False)
    subscribe = forms.BooleanField(label=_("Subscribe via email"), required=False)

