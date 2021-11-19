from rest_framework import serializers
from ucbox_plugin import models
from netbox.api import WritableNestedSerializer
from tenancy.api.nested_serializers import NestedTenantSerializer

__all__ = ["NestedNumberSerializer", "NestedTrunkSerializer"]


class NestedNumberSerializer(WritableNestedSerializer):

    label = serializers.CharField(source='number', read_only=True)
    tenant = NestedTenantSerializer(required=True, allow_null=False)

    class Meta:
        model = models.Number
        fields = [
            "id", "label", "number", "tenant",
        ]

class NestedTrunkSerializer(WritableNestedSerializer):

    label = serializers.CharField(source='trunk', read_only=True)
    tenant = NestedTenantSerializer(required=True, allow_null=False)

    class Meta:
        model = models.Trunk
        fields = [
            "id", "label", "trunk", "tenant",
        ]
