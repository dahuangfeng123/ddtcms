from django.contrib import admin
from ddtcms.link.models import Link
from ddtcms.link.models import Category
from ddtcms.link.models import CGPUpload

class LinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'url','category', 'slug',  'pub_date')
    list_filter = ('category', 'domain')
    ordering = ('url',)
    search_fields = ('title', 'url')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'user','slug','display_order')
    list_filter = ('user',)
class CGPUploadAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        return False # To remove the 'Save and continue editing' button
        
        
admin.site.register(Link, LinkAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(CGPUpload,CGPUploadAdmin)



