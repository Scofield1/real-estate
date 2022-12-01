from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *


class AgentAdmin(ImportExportModelAdmin):
    list_display = ['f_name', 'l_name']


class PropertyAdmin(ImportExportModelAdmin):
    list_display = ['name', 'agent', 'location']


class PropertyAmenityAdmin(ImportExportModelAdmin):
    pass


class PropertyStatusAdmin(ImportExportModelAdmin):
    pass


class PropertyTypeAdmin(ImportExportModelAdmin):
    pass


class PropertyImageAdmin(ImportExportModelAdmin):
    pass


admin.site.register(Agent, AgentAdmin)
admin.site.register(Property, PropertyAdmin)
admin.site.register(PropertyAmenity, PropertyAmenityAdmin)
admin.site.register(PropertyStatus, PropertyStatusAdmin)
admin.site.register(PropertyType, PropertyTypeAdmin)
admin.site.register(PropertyImage, PropertyImageAdmin)
