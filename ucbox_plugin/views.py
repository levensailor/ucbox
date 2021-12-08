#!./venv/bin/python

from netbox.views import generic
from .models import Number, Trunk, UCCluster, DevicePool
from . import filters
from . import forms
from . import tables

from django.conf import settings
from packaging import version


NETBOX_CURRENT_VERSION = version.parse(settings.VERSION)


class NumberListView(generic.ObjectListView):
    queryset = Number.objects.all()
    filterset = filters.NumberFilterSet
    filterset_form = forms.NumberFilterForm
    table = tables.NumberTable
    if NETBOX_CURRENT_VERSION >= version.parse("3.0"):
        template_name = "ucbox_plugin/number_list_view_3.x.html"
    else:
        template_name = "ucbox_plugin/number_list_view.html"


class NumberView(generic.ObjectView):
    queryset = Number.objects.prefetch_related('tenant')
    if NETBOX_CURRENT_VERSION >= version.parse("3.0"):
        template_name = "ucbox_plugin/number_3.x.html"
    else:
        template_name = "ucbox_plugin/number.html"


class NumberEditView(generic.ObjectEditView):
    queryset = Number.objects.all()
    model_form = forms.NumberEditForm
    if NETBOX_CURRENT_VERSION >= version.parse("3.0"):
        template_name = "ucbox_plugin/add_number_3.x.html"
    else:
        template_name = "ucbox_plugin/add_number.html"


class NumberBulkEditView(generic.BulkEditView):
    queryset = Number.objects.prefetch_related('tenant')
    filterset = filters.NumberFilterSet
    table = tables.NumberTable
    form = forms.NumberBulkEditForm


class NumberDeleteView(generic.ObjectDeleteView):
    queryset = Number.objects.all()
    default_return_url = "plugins:ucbox_plugin:number_list_view"


class NumberBulkDeleteView(generic.BulkDeleteView):
    queryset = Number.objects.filter()
    filterset = filters.NumberFilterSet
    table = tables.NumberTable
    default_return_url = "plugins:ucbox_plugin:number_list_view"


class NumberBulkImportView(generic.BulkImportView):
    queryset = Number.objects.all()
    model_form = forms.NumberCSVForm
    table = tables.NumberTable


class TrunkListView(generic.ObjectListView):
    queryset = Trunk.objects.all()
    filterset = filters.TrunkFilterSet
    filterset_form = forms.TrunkFilterForm
    table = tables.TrunkTable
    if NETBOX_CURRENT_VERSION >= version.parse("3.0"):
        template_name = "ucbox_plugin/trunk_list_view_3.x.html"
    else:
        template_name = "ucbox_plugin/trunk_list_view.html"


class TrunkView(generic.ObjectView):
    queryset = Trunk.objects.prefetch_related('tenant')
    if NETBOX_CURRENT_VERSION >= version.parse("3.0"):
        template_name = "ucbox_plugin/trunk_3.x.html"
    else:
        template_name = "ucbox_plugin/trunk.html"


class TrunkEditView(generic.ObjectEditView):
    queryset = Trunk.objects.all()
    model_form = forms.TrunkEditForm
    if NETBOX_CURRENT_VERSION >= version.parse("3.0"):
        template_name = "ucbox_plugin/add_trunk_3.x.html"
    else:
        template_name = "ucbox_plugin/add_trunk.html"


class TrunkBulkEditView(generic.BulkEditView):
    queryset = Trunk.objects.prefetch_related('tenant')
    filterset = filters.TrunkFilterSet
    table = tables.TrunkTable
    form = forms.TrunkBulkEditForm


class TrunkDeleteView(generic.ObjectDeleteView):
    queryset = Trunk.objects.all()
    default_return_url = "plugins:ucbox_plugin:trunk_list_view"


class TrunkBulkDeleteView(generic.BulkDeleteView):
    queryset = Trunk.objects.filter()
    filterset = filters.TrunkFilterSet
    table = tables.TrunkTable
    default_return_url = "plugins:ucbox_plugin:trunk_list_view"


class TrunkBulkImportView(generic.BulkImportView):
    queryset = Trunk.objects.all()
    model_form = forms.TrunkCSVForm
    table = tables.TrunkTable




class UCClusterListView(generic.ObjectListView):
    queryset = UCCluster.objects.all()
    filterset = filters.UCClusterFilterSet
    filterset_form = forms.UCClusterFilterForm
    table = tables.UCClusterTable
    if NETBOX_CURRENT_VERSION >= version.parse("3.0"):
        template_name = "ucbox_plugin/uccluster_list_view_3.x.html"
    else:
        template_name = "ucbox_plugin/uccluster_list_view.html"


class UCClusterView(generic.ObjectView):
    queryset = UCCluster.objects.prefetch_related('tenant')
    if NETBOX_CURRENT_VERSION >= version.parse("3.0"):
        template_name = "ucbox_plugin/uccluster_3.x.html"
    else:
        template_name = "ucbox_plugin/uccluster.html"


class UCClusterEditView(generic.ObjectEditView):
    queryset = UCCluster.objects.all()
    model_form = forms.UCClusterEditForm
    if NETBOX_CURRENT_VERSION >= version.parse("3.0"):
        template_name = "ucbox_plugin/add_uccluster_3.x.html"
    else:
        template_name = "ucbox_plugin/add_uccluster.html"


class UCClusterBulkEditView(generic.BulkEditView):
    queryset = UCCluster.objects.prefetch_related('tenant')
    filterset = filters.UCClusterFilterSet
    table = tables.UCClusterTable
    form = forms.UCClusterBulkEditForm


class UCClusterDeleteView(generic.ObjectDeleteView):
    queryset = UCCluster.objects.all()
    default_return_url = "plugins:ucbox_plugin:uccluster_list_view"


class UCClusterBulkDeleteView(generic.BulkDeleteView):
    queryset = UCCluster.objects.filter()
    filterset = filters.UCClusterFilterSet
    table = tables.UCClusterTable
    default_return_url = "plugins:ucbox_plugin:uccluster_list_view"


class UCClusterBulkImportView(generic.BulkImportView):
    queryset = UCCluster.objects.all()
    model_form = forms.UCClusterCSVForm
    table = tables.UCClusterTable


class DevicePoolListView(generic.ObjectListView):
    queryset = DevicePool.objects.all()
    filterset = filters.DevicePoolFilterSet
    filterset_form = forms.DevicePoolFilterForm
    table = tables.DevicePoolTable
    if NETBOX_CURRENT_VERSION >= version.parse("3.0"):
        template_name = "ucbox_plugin/devicepool_list_view_3.x.html"
    else:
        template_name = "ucbox_plugin/devicepool_list_view.html"


class DevicePoolView(generic.ObjectView):
    queryset = DevicePool.objects.prefetch_related('tenant')
    if NETBOX_CURRENT_VERSION >= version.parse("3.0"):
        template_name = "ucbox_plugin/devicepool_3.x.html"
    else:
        template_name = "ucbox_plugin/devicepool.html"


class DevicePoolEditView(generic.ObjectEditView):
    queryset = DevicePool.objects.all()
    model_form = forms.DevicePoolEditForm
    if NETBOX_CURRENT_VERSION >= version.parse("3.0"):
        template_name = "ucbox_plugin/add_devicepool_3.x.html"
    else:
        template_name = "ucbox_plugin/add_devicepool.html"


class DevicePoolBulkEditView(generic.BulkEditView):
    queryset = DevicePool.objects.prefetch_related('tenant')
    filterset = filters.DevicePoolFilterSet
    table = tables.DevicePoolTable
    form = forms.DevicePoolBulkEditForm


class DevicePoolDeleteView(generic.ObjectDeleteView):
    queryset = DevicePool.objects.all()
    default_return_url = "plugins:ucbox_plugin:devicepool_list_view"


class DevicePoolBulkDeleteView(generic.BulkDeleteView):
    queryset = DevicePool.objects.filter()
    filterset = filters.DevicePoolFilterSet
    table = tables.DevicePoolTable
    default_return_url = "plugins:ucbox_plugin:devicepool_list_view"


class DevicePoolBulkImportView(generic.BulkImportView):
    queryset = DevicePool.objects.all()
    model_form = forms.DevicePoolCSVForm
    table = tables.DevicePoolTable
