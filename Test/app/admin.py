from django.contrib import admin

# Register your models here.
from app.models import Menu, MenuItem

# admin.site.register(Menu)
# admin.site.register(MenuItem)

class MenuItemInline(admin.TabularInline):
    model = MenuItem
    exclude = ['has_children']
    ordering = ('order',)



class MenuAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    inlines = [MenuItemInline,]



admin.site.register(Menu, MenuAdmin)