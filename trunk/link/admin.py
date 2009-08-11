from django.contrib import admin
from ddtcms.link.models import Link
from ddtcms.link.models import Category

class LinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'url','category', 'slug',  'pub_date')
    list_filter = ('title', 'domain')
    ordering = ('url',)
    search_fields = ('title', 'url')

admin.site.register(Link, LinkAdmin)
admin.site.register(Category)



