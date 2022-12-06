from import_export import resources
from .models import *


class AgentResource(resources.ModelResource):
    class Meta:
        model = Agent


class PropertyResource(resources.ModelResource):
    class Meta:
        model = Property


class PropertyStatusResource(resources.ModelResource):
    class Meta:
        model = PropertyStatus


class PropertyTypeResource(resources.ModelResource):
    class Meta:
        model = PropertyType


class PropertyAmenityResource(resources.ModelResource):
    class Meta:
        model = PropertyAmenity


class PropertyImageResource(resources.ModelResource):
    class Meta:
        model = PropertyImage