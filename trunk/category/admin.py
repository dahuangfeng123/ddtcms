from django.contrib import admin
from django.conf import settings

from django.utils.translation import ugettext_lazy as _
from ddtcms.category.models import Category

class CategoryAdmin(admin.ModelAdmin):
    fieldsets = (
        (None,
           {'fields': ('content_type', 'object_pk', 'site')}
        ),
        (_('Content'),
           {'fields': ('user', 'name', 'root_pk', 'display_order')}
        ),
     )

    list_display = ('name', 'content_type', 'object_pk', 'user', 'display_order', 'root_pk')
    list_filter = ('user', 'site', 'root_pk')
    ordering = ('content_type',)
    search_fields = ('name', 'user__username')

admin.site.register(Category, CategoryAdmin)
