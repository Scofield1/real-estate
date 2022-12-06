from import_export import resources
from .models import *


class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category


class BlogResource(resources.ModelResource):
    class Meta:
        model = BlogModel