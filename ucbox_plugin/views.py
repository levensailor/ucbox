#!./venv/bin/python

from netbox.views import generic
from .models import Number, Trunk
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
    default_return_url = "plugins:ucbox_plugin:list_view"


class NumberBulkDeleteView(generic.BulkDeleteView):
    queryset = Number.objects.filter()
    filterset = filters.NumberFilterSet
    table = tables.NumberTable
    default_return_url = "plugins:ucbox_plugin:list_view"


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
    default_return_url = "plugins:ucbox_plugin:list_view"


class TrunkBulkDeleteView(generic.BulkDeleteView):
    queryset = Trunk.objects.filter()
    filterset = filters.TrunkFilterSet
    table = tables.TrunkTable
    default_return_url = "plugins:ucbox_plugin:list_view"


class TrunkBulkImportView(generic.BulkImportView):
    queryset = Trunk.objects.all()
    model_form = forms.TrunkCSVForm
    table = tables.TrunkTable
