from django.contrib import admin
from .models import Number, Trunk


@admin.register(Number)
class NumPlanAdmin(admin.ModelAdmin):
    list_display = ("number", "tenant", "description", "provider", "forward_to")

@admin.register(Trunk)
class TrunkPlanAdmin(admin.ModelAdmin):
    list_display = ("trunk", "tenant", "destination", "provider", "region", "description")