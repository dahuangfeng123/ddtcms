from django.contrib import admin
from django.conf import settings

from django.utils.translation import ugettext_lazy as _
from ddtcms.category.models import Category

 


class CategoryAdmin(admin.ModelAdmin):
    fieldsets = (
        (None,
           {'fields': ('content_type',  'site')}
        ),
        (_('Content'),
           {'fields': ('user', 'name', 'parent', 'root_pk', 'display_order')}
        ),
     )
    #date_hierarchy = 'pub_date'
    list_display = ('name','parent','content_type',  'user', 'display_order', 'root_pk')
    list_filter = ('user','parent','root_pk')
    ordering = ('content_type',)
    search_fields = ('name', 'user__username')

admin.site.register(Category, CategoryAdmin)
