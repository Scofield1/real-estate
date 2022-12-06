from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin


class CategoryAdmin(ImportExportModelAdmin):
    list_display = ['name']


class BlogAdmin(ImportExportModelAdmin):
    list_display = ['user', 'title']


admin.site.register(Category, CategoryAdmin)
admin.site.register(BlogModel, BlogAdmin)
