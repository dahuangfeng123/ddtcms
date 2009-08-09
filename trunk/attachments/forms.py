from django import forms
from attachments.models import Attachment
from django.forms import FileInput
from django.conf import settings
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string
from django.utils.translation import ugettext as _

class DynamicMultipleFileField(FileInput):

    #class Media:
    #    js = ("%seditor/nicEdit/nicEdit.js" % settings.MEDIA_URL,)

    def __init__(self,  attrs=None): 
        self.attrs = {'class': 'DynamicMultipleFileField','size':'50'}       
        if attrs is not None:
            self.attrs.update(attrs)
        #super(DynamicMultipleFileField, self).__init__(attrs)

    def render(self, name, value, attrs=None):
        rendered = super(DynamicMultipleFileField, self).render(name, value, attrs)
        context = {
            'name': name,
        }
        return rendered  + mark_safe(render_to_string('attachments\danamicmutiplefilefield.html', context))
        #return mark_safe(render_to_string('attachments\danamicmutiplefilefield.html', context))

class AttachmentForm(forms.ModelForm):
    
    class Meta:
        model = Attachment
        exclude = ('content_type', 'object_id', 'attached_by')
        
class AttachmentUploadForm(forms.Form):
    title = forms.CharField(label=_("Title"),  widget=forms.TextInput(attrs={'size': 50,'class': 'required'}),  max_length=100,help_text="max_length is 100")
    body = forms.CharField(label=_("Body"), widget=forms.Textarea(attrs={'rows':8, 'cols':50})) 
    file =  forms.FileField(label=_("Files"))
    
