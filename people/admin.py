from django.contrib import admin
from ddtcms.people.models import Person,Contact,Organization

class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name','parent','order')

class PersonAdmin(admin.ModelAdmin):
    list_display = ('fullname','country','is_easterner')

class ContactAdmin(admin.ModelAdmin):
    list_display = ('person','mobile')


admin.site.register(Organization,OrganizationAdmin)
admin.site.register(Person,PersonAdmin)
admin.site.register(Contact,ContactAdmin)

