from django.contrib import admin
from .models import Number, Trunk, UCCluster, DevicePool


@admin.register(Number)
class NumPlanAdmin(admin.ModelAdmin):
    list_display = ("number", "tenant", "description", "provider", "forward_to")

@admin.register(Trunk)
class TrunkPlanAdmin(admin.ModelAdmin):
    list_display = ("trunk", "tenant", "destination", "provider", "region", "description")

@admin.register(UCCluster)
class UCClusterPlanAdmin(admin.ModelAdmin):
    list_display = ("uccluster", "tenant", "description", "publisher", "subscriber1", "subscriber2", "subscriber3", "subscriber4", "tftp1", "tftp2")

@admin.register(DevicePool)
class DevicePoolPlanAdmin(admin.ModelAdmin):
    list_display = ("devicepool", "tenant", "region", "description", "datetimegroup", "localroutegroup", "cmgroup")