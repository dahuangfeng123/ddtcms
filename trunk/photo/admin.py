from ddtcms.photo.models import Photo

from django.contrib import admin


class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['topic']}),

    ]

    list_display = ('topic')
    list_filter = ['topic']
    search_fields = ['topic']
    #date_hierarchy = 'pub_date'


admin.site.register(Photo)
