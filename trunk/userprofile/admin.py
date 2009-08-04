from django.contrib import admin
from userprofile.models import EmailValidation, Avatar
from userprofile.models import Profile,Resume,Favourite

class EmailValidationAdmin(admin.ModelAdmin):
    list_display = ('__unicode__',)
    search_fields = ('user__username', 'user__first_name')

admin.site.register(Avatar)
admin.site.register(EmailValidation, EmailValidationAdmin)
admin.site.register(Profile)
admin.site.register(Resume)
admin.site.register(Favourite)
