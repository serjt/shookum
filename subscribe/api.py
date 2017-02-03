from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from .models import *


class FileResource(ModelResource):
    class Meta:
        queryset = File.objects.all()
        resource_name = 'files'
