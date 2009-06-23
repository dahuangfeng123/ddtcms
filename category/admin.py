from django.contrib import admin
from django.conf import settings

from django.utils.translation import ugettext_lazy as _
from ddtcms.category.models import Category,Outline

 
class OutlineAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name','slug')
    list_filter = ('name','slug')
    ordering = ('content_type',)
    search_fields = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    fieldsets = (
        (None,
           {'fields': ('outline','user' )}
        ),
        (_('Content'),
           {'fields': ( 'name', 'slug','parent', 'root_pk', 'display_order')}
        ),
     )
    #date_hierarchy = 'pub_date'
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name','parent','user', 'display_order', 'root_pk')
    list_filter = ('user','parent','root_pk')
    ordering = ('outline',)
    search_fields = ('name', 'user__username')

admin.site.register(Outline, OutlineAdmin)
admin.site.register(Category, CategoryAdmin)
