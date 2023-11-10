from django.contrib import admin

from tree_menu.models import Item, Menu


@admin.register(Item)
class MenuItemAdmin(admin.ModelAdmin):

    list_display = ('title', 'parent')
    list_filter = ('menu',)
    search_fields = ('title',)


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):

    list_display = ('title', 'slug')
    search_fields = ('title', 'slug')
