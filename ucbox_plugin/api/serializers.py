from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from ..models import Number, Trunk, UCCluster, DevicePool
from tenancy.api.nested_serializers import NestedTenantSerializer
from dcim.api.nested_serializers import NestedRegionSerializer
from circuits.api.nested_serializers import NestedProviderSerializer
from extras.api.serializers import TagSerializer
from .nested_serializers import NestedNumberSerializer, NestedTrunkSerializer, NestedUCClusterSerializer, NestedDevicePoolSerializer
from extras.api.nested_serializers import NestedTagSerializer


class NumberSerializer(TagSerializer, serializers.ModelSerializer):

    label = serializers.CharField(source='number', read_only=True)
    tenant = NestedTenantSerializer(required=True, allow_null=False)
    region = NestedRegionSerializer(required=False, allow_null=True)
    provider = NestedProviderSerializer(required=False, allow_null=True)
    forward_to = NestedNumberSerializer(required=False, allow_null=True)
    tags = NestedTagSerializer(many=True, required=False)

    class Meta:
        model = Number
        fields = [
            "id", "label", "number", "tenant", "region", "forward_to", "description", "provider", "tags",
        ]

class TrunkSerializer(TagSerializer, serializers.ModelSerializer):

    label = serializers.CharField(source='trunk', read_only=True)
    tenant = NestedTenantSerializer(required=True, allow_null=False)
    region = NestedRegionSerializer(required=False, allow_null=True)
    provider = NestedProviderSerializer(required=False, allow_null=True)
    tags = NestedTagSerializer(many=True, required=False)

    class Meta:
        model = Trunk
        fields = [
            "id", "label", "trunk", "tenant", "region", "destination", "description", "provider", "tags",
        ]

class UCClusterSerializer(TagSerializer, serializers.ModelSerializer):

    label = serializers.CharField(source='uccluster', read_only=True)
    tenant = NestedTenantSerializer(required=True, allow_null=False)
    tags = NestedTagSerializer(many=True, required=False)

    class Meta:
        model = UCCluster
        fields = [
            "id", "label", "uccluster", "tenant", "publisher", "subscriber1", "subscriber2", "subscriber3", "subscriber4", "tftp1", "tftp2", "description", "tags"
        ]

class DevicePoolSerializer(TagSerializer, serializers.ModelSerializer):

    label = serializers.CharField(source='devicepool', read_only=True)
    tenant = NestedTenantSerializer(required=True, allow_null=False)
    region = NestedRegionSerializer(required=False, allow_null=True)
    tags = NestedTagSerializer(many=True, required=False)

    class Meta:
        model = DevicePool
        fields = [
            "id", "label", "devicepool", "tenant", "region", "description", "datetimegroup", "localroutegroup", "cmgroup", "tags",
        ]