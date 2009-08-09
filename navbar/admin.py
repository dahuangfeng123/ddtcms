from django.contrib import admin

from navbar.models import NavBarItem

class NavBarItemAdmin(admin.ModelAdmin):
        fieldsets = (
            (None, {'fields': ('name', 'title', 'url', 'order', 'parent')}),
            ('Advanced Permissions', {'classes': ('collapse',),
                             'fields': ('path_type', 'user_type', 'groups', )}),
        )
        list_filter = ('parent',)
        list_display = ('name', 'url', 'order', 'parent','user_type')
        search_fields = ('url', 'name', 'title')
        filter_horizontal = ("groups",)

admin.site.register(NavBarItem, NavBarItemAdmin)
