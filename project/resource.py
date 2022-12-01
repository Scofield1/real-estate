from import_export import resources
from .models import *


class AgentResource(resources.ModelResource):
    class Meta:
        model = Agent