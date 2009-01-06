from ddtcms.wiki.models import Wiki
from django.contrib import admin

class WikiAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['pagename']}),
        ('Date information', {'fields': ['pub_date']}),
        ('Wiki Content',     {'fields': ['content']}),
    ]

    list_display = ('pagename', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['pagename']
    date_hierarchy = 'pub_date'






admin.site.register(Wiki, WikiAdmin)



