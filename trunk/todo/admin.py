from django.contrib import admin
from ddtcms.todo.models import Project,Task


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name','slug','tasks','pub_date') 
    
    
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name','project','lastupdated','priority','completed')
    list_filter =('project',)     

admin.site.register(Project,ProjectAdmin)
admin.site.register(Task,TaskAdmin)