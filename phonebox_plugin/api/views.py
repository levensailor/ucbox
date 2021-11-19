from rest_framework.routers import APIRootView
from .. import filters
from ..models import Number, Trunk
from netbox.api.views import ModelViewSet
from . import serializers


class UCBoxPluginRootView(APIRootView):
    """
    ucbox_plugin API root view
    """
    def get_view_name(self):
        return 'UCBox'


class NumberViewSet(ModelViewSet):
    queryset = Number.objects.prefetch_related('tenant', 'region', 'tags')
    serializer_class = serializers.NumberSerializer
    filterset_class = filters.NumberFilterSet

class TrunkViewSet(ModelViewSet):
    queryset = Trunk.objects.prefetch_related('tenant', 'region', 'tags')
    serializer_class = serializers.TrunkSerializer
    filterset_class = filters.TrunkFilterSet