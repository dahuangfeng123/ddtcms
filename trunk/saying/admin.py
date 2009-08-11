from django.contrib import admin
from ddtcms.saying.models import Saying



class SayingAdmin(admin.ModelAdmin):
    list_display = ('sayer', 'said_date')
    list_filter = ['pub_date']
    search_fields = ['content']
    date_hierarchy = 'pub_date'






admin.site.register(Saying, SayingAdmin)



