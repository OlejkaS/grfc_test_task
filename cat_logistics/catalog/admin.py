from django.contrib import admin

from .models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display: tuple[str] = ('name', 'parent')
    search_fields: tuple[str] = ('name',)
    list_filter: tuple[str] = ('name',)
