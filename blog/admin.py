# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from django import forms
from ddtcms.blog.models import Entry
from ddtcms.category.models import Category


class BlogEntryAdminForm(forms.ModelForm):
    BLOOD_CHOICES = (
        (u'A型', u'A型'),
        (u'B型', u'B型'),
        (u'O型', u'O型'),
        (u'AB型',u'AB型'),
    )
    class Meta:
        model = Entry


class EntryAdmin(admin.ModelAdmin):
    #form = BlogEntryAdminForm
    
    #http://code.djangoproject.com/wiki/NewformsHOWTO
    #Lllama's handy how-do-I guide to newforms admin.
    #Q: How do I filter the ChoiceField? based upon attributes of the current ModelAdmin? instance? 
    #Ticket #3987 http://code.djangoproject.com/ticket/3987
    #
    def __call__(self, request, url):
        #Add in the request object, so that it may be referenced
        #later in the formfield_for_dbfield function.
        self.request = request
        return super(EntryAdmin, self).__call__(request, url)
    
    def formfield_for_dbfield(self, db_field, **kwargs):
        field = super(EntryAdmin, self).formfield_for_dbfield(db_field, **kwargs) # Get the default field
        if db_field.name == 'category': 
            #Add the null object
            my_choices = [('', '---------')]
            #Grab the current site id from the URL.
            my_choices.extend(Category.objects.filter(user=self.request.user).values_list('id','name'))
            #print my_choices
            field.choices = my_choices
        return field

    
    def queryset(self, request):
        if request.user.is_superuser:
            return super(EntryAdmin, self).queryset(request)
        else:
            queries = {'user':request.user}
            return super(EntryAdmin, self).queryset(request).filter(**queries)
            

    
    #
    #CODE FROM :
    #URL:  http://code.djangoproject.com/wiki/CookBookNewformsAdminAndUser
    #TITLE:How to set the current user on the model instance in the admin (newforms-admin) 
    #
    def save_model(self, request, obj, form, change): 
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        form.save_m2m()
        return instance

    def save_formset(self, request, form, formset, change): 
        def set_user(instance):
            instance.user = request.user
            instance.save()

        if formset.model == Comment:
            instances = formset.save(commit=False)
            map(set_user, instances)
            formset.save_m2m()
            return instances
        else:
            return formset.save()

    
    fieldsets = [
        ('标题',             {'fields': ['title']}),
        ('简短标记',         {'fields': ['slug']}),
        #('所属用户',         {'fields': ['user']}),
        ('所属分类',         {'fields': ['category']}),
        ('Date information', {'fields': ['pub_date']}),
        ('内容',             {'fields': ['content']}),
        ('摘要',             {'fields': ['summary']}),
        ('Tags',             {'fields': ['tags']}), 
        ('Views',            {'fields': ['views']}),
        ('Comments',         {'fields': ['comments']}), 
    ]

    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'user','category','pub_date')
    list_filter = ['pub_date']
    search_fields = ['title','user' ,'summary', 'content']
    date_hierarchy = 'pub_date'
    
    



admin.site.register(Entry,EntryAdmin)
