
from django.contrib import admin
from django.forms import widgets
from django.utils.translation import ugettext_lazy as _

from categories.models import Category
from categories.models import CategoryItem

class CategoryInline(admin.TabularInline):
    model = Category
    fields = ('sort_order', 'name', 'slug',)
    verbose_name_plural = _('Children Categories')
    ordering = ('')
    
    prepopulated_fields = {
        'slug': ('name',)
    }
    
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'sort_order':
            kwargs['widget'] = widgets.TextInput(attrs=dict(size=5))
        return super(CategoryInline, self).formfield_for_dbfield(db_field, **kwargs)

class CategoryAdmin(admin.ModelAdmin):
    
    list_display = ('breadcrumbs',)
    
    #inlines = (
    #    # CategoryInline,
    #)
    #inlines = [CategoryInline]
    prepopulated_fields = {
        'slug': ('name',)
    }
    
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'sort_order':
            kwargs['widget'] = widgets.TextInput(attrs=dict(size=5))
        return super(CategoryAdmin, self).formfield_for_dbfield(db_field, **kwargs)


admin.site.register(Category, CategoryAdmin)
admin.site.register(CategoryItem)   