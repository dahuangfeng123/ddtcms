from django.contrib import admin
from ddtcms.notice.models import Notice

class NoticeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug','type','pub_date','over_date')
    list_filter = ['type']
    search_fields = ['title','slug']
    

admin.site.register(Notice,NoticeAdmin)

