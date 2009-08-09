# -*- coding: utf-8 -*-
from django.contrib import admin
from ddtcms.news.models import News
from ddtcms.news.models import Category


from django.core.urlresolvers import reverse
from django import forms


class NewsAdmin(admin.ModelAdmin):
  
    def __call__(self, request, url):
        #Add in the request object, so that it may be referenced
        #later in the formfield_for_dbfield function.
        self.request = request
        return super(NewsAdmin, self).__call__(request, url)
    
    def formfield_for_dbfield(self, db_field, **kwargs):
        field = super(NewsAdmin, self).formfield_for_dbfield(db_field, **kwargs) # Get the default field
        if db_field.name == 'category': 
            #Add the null object
            my_choices = [('', '---------')]
            #Grab the current site id from the URL.
            my_choices.extend(Category.objects.values_list('id','name'))
            #print my_choices
            field.choices = my_choices
            return field
        return super(NewsAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        

    
    def queryset(self, request):
        if request.user.is_superuser:
            return super(NewsAdmin, self).queryset(request)
        else:
            queries = {'user':request.user}
            return super(NewsAdmin, self).queryset(request).filter(**queries)
  
    def save_model(self, request, obj, form, change): 
        instance = form.save(commit=False)
        instance.user = request.user
        instance.editor = request.user.username
        instance.save()
        form.save_m2m()
        return instance

    def save_formset(self, request, form, formset, change): 
        def set_user(instance):
            instance.user = request.user
            instance.editor = request.user.username
            instance.save()

        if formset.model == Comment:
            instances = formset.save(commit=False)
            map(set_user, instances)
            formset.save_m2m()
            return instances
        else:
            return formset.save()

    
    fieldsets = [
        ('标题',             {'fields': ['title','subtitle','slug']}),
        ('基本信息(必填,请认真选择)',         {'fields': ['category','source','deliverer']}),
        ('日期和时间',       {'classes': ('collapse',),'fields': ['pub_date']}),
        ('内容',             {'fields': ['content']}),
        ('摘要',             {'fields': ['summary']}),
        ('Tags',             {'fields': ['tags']}), 
        ('查阅数',            {'fields': ['views']}),
        ('评论数',         {'fields': ['comments']}), 
        ('是否允许评论',         {'fields': ['allow_comments']}),        	
        ('责任编辑',         {'fields': ['editor']}),
        ('选项',         {'fields': ['status']}), 	
        ('新闻指示图片',         {'fields': ['pic']}), 
    ]

    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug','deliverer','category','pub_date','status','is_pic')
    list_filter = ['pub_date','status']
    search_fields = ['title','deliverer' ,'summary', 'content']
    date_hierarchy = 'pub_date'
    
    
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'slug','parent','path','depth','posts','order')
    list_filter = ['slug']
    search_fields = ['title','slug']
    


    


admin.site.register(News,NewsAdmin)
admin.site.register(Category,CategoryAdmin)

