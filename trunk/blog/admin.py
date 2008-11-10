# -*- coding: utf-8 -*-
from django.contrib import admin
from ddtcms.blog.models import Category
from ddtcms.blog.models import Entry
from ddtcms.blog.models import Tag

#class TagInline(admin.TabularInline):#StackedInline):
#    model = Tag
#    extra = 3

class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        ("所属用户",         {'fields': ['user']}),
        ("简短标记",         {'fields': ['slug']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
#    inlines = [EntryInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name']
    date_hierarchy = 'pub_date'



class EntryAdmin(admin.ModelAdmin):
    fieldsets = [
        ("标题",             {'fields': ['title']}),
        ('简短标记',         {'fields': ['slug']}),
        ("所属用户",         {'fields': ['user']}),
        ("所属分类",         {'fields': ['category']}),
        ('Date information', {'fields': ['pub_date']}),
        ('内容',             {'fields': ['content']}),
        ('摘要',             {'fields': ['summary']}),
        ('Tags',             {'fields': ['tags']}), 
        
    ]
#    inlines = [TagInline]
    list_display = ('title', 'category','pub_date')
    list_filter = ['pub_date']
    search_fields = ['title','user' ,'summary', 'content']
    date_hierarchy = 'pub_date'
    

admin.site.register(Category, CategoryAdmin)
#admin.site.register(Category)
admin.site.register(Entry,EntryAdmin)
admin.site.register(Tag)
#admin.site.register(CategoryAdmin)this is wrong