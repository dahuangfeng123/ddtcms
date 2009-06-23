from django.contrib import admin
from ddtcms.link.models import Link

class LinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'url','category', 'slug',  'pub_date')
    list_filter = ('name', 'domain')
    ordering = ('url',)
    search_fields = ('name', 'url')

admin.site.register(Link, LinkAdmin)



