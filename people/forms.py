# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _
from datetime import datetime
from ddtcms.people.models import Person,Category
# I put this on all required fields, because it's easier to pick up
# on them with CSS or JavaScript if they have a class of "required"
# in the HTML. Your mileage may vary. If/when Django ticket #3515
# lands in trunk, this will no longer be necessary.
attrs_dict = { 'class': 'required' }

from attachments.forms import DynamicMultipleFileField
from ddtcms.forum.forms import NicEditor

def category_choices():
    my_choices = [] 
    for c in Category.objects.get_all_roots():
        tc=c.name,tuple(c.get_children().values_list('id','name'))
        my_choices.append(tc)
    return my_choices

class NewsForm(forms.ModelForm):
    category  = forms.ChoiceField(label=_(u"Category"),  choices=category_choices(),help_text="News Items Canot addto Top level Category")
    deliverer = forms.CharField(label=_(u"Deliverer"))   
    content   = forms.CharField(label=_(u"Content"), widget=NicEditor(attrs={'rows':15, 'cols':66}),required=True)   
    file      = forms.FileField(label=_("Files"),widget=DynamicMultipleFileField(), required=False)	

    class Meta:
        model = News
        #exclude = ('status', 'editor', 'attached_by', 'allow_comments','views','comments','pic')
        exclude = ('editor','views','comments')


    def clean_title(self):
        # do something that validates your data
        return self.cleaned_data["title"]
    
    def clean_category(self):
        # do something that validates your data
        category = self.cleaned_data.get("category")

        #if Category.objects.filter(name__iexact=category).count() == 0:
        cc=category.child.count()
        if cc == 0:    
            return self.cleaned_data["category"]
        else:
            raise forms.ValidationError(_("The category has child(ren),you must select one of its child!"))
        return self.cleaned_data["category"]