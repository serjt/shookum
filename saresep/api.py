from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from .models import *


class SaresepResource(ModelResource):
    class Meta:
        queryset = File.objects.order_by('date')
        resource_name = 'saresep/files'
