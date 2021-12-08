from django import forms
from utilities.forms import (
    BootstrapMixin, DynamicModelMultipleChoiceField, DynamicModelChoiceField,
    TagFilterField, BulkEditForm, CSVModelForm, CSVModelChoiceField
)
from extras.forms import AddRemoveTagsForm
from tenancy.models import Tenant
from dcim.models import Region
from circuits.models import Provider
from extras.models import Tag
from .models import Number, Trunk, UCCluster, DevicePool


class NumberFilterForm(BootstrapMixin, forms.Form):

    model = Number
    q = forms.CharField(
        required=False,
        label='Search'
    )
    tenant = DynamicModelMultipleChoiceField(
        queryset=Tenant.objects.all(),
        to_field_name='id',
        required=False,
        null_option='None',
    )
    region = DynamicModelMultipleChoiceField(
        queryset=Region.objects.all(),
        to_field_name='id',
        required=False,
        null_option='None',
    )
    provider = DynamicModelMultipleChoiceField(
        queryset=Provider.objects.all(),
        to_field_name='id',
        required=False,
        null_option='None',
    )
    tag = TagFilterField(model)


class NumberEditForm(BootstrapMixin, forms.ModelForm):

    number = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'autocomplete': 'off',
                'pattern': r'^\+?[0-9A-D\*\#]+$',
                'title': 'Enter the Phone Number'
            }
        )
    )
    tags = DynamicModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        required=False
    )

    class Meta:
        model = Number
        fields = ('number', 'tenant', 'region', 'description', 'provider', 'forward_to', 'tags')


class NumberBulkEditForm(BootstrapMixin, AddRemoveTagsForm, BulkEditForm):

    pk = forms.ModelMultipleChoiceField(
        queryset=Number.objects.all(),
        widget=forms.MultipleHiddenInput()
    )
    tenant = DynamicModelChoiceField(
        queryset=Tenant.objects.all(),
        to_field_name='id',
        required=False,
        null_option='None',
    )
    region = DynamicModelChoiceField(
        queryset=Region.objects.all(),
        to_field_name='id',
        required=False,
        null_option='None',
    )
    provider = DynamicModelChoiceField(
        queryset=Provider.objects.all(),
        to_field_name='id',
        required=False,
        null_option='None',
    )
    # Implement plugin API to migrate to DynamicModelChoiceField
    forward_to = forms.ModelChoiceField(
        queryset=Number.objects.all(),
        to_field_name="number",
        required=False
    )
    description = forms.CharField(
        max_length=200,
        required=False
    )

    class Meta:
        nullable_fields = ('region', 'provider', 'forward_to', 'description')


class NumberCSVForm(CSVModelForm):
    tenant = CSVModelChoiceField(
        queryset=Tenant.objects.all(),
        required=True,
        to_field_name='name',
        help_text='Assigned tenant'
    )
    provider = CSVModelChoiceField(
        queryset=Provider.objects.all(),
        to_field_name='name',
        required=False,
        help_text='Originating provider'
    )
    region = CSVModelChoiceField(
        queryset=Region.objects.all(),
        required=False,
        to_field_name='name',
        help_text='Assigned region'
    )
    forward_to = CSVModelChoiceField(
        queryset=Number.objects.all(),
        to_field_name="number",
        required=False
    )

    class Meta:
        model = Number
        fields = Number.csv_headers
        help_texts = {
            'forward_to': "Optional call forwarding Number",
        }


class TrunkFilterForm(BootstrapMixin, forms.Form):

    model = Trunk
    q = forms.CharField(
        required=False,
        label='Search'
    )
    tenant = DynamicModelMultipleChoiceField(
        queryset=Tenant.objects.all(),
        to_field_name='id',
        required=False,
        null_option='None',
    )
    region = DynamicModelMultipleChoiceField(
        queryset=Region.objects.all(),
        to_field_name='id',
        required=False,
        null_option='None',
    )
    provider = DynamicModelMultipleChoiceField(
        queryset=Provider.objects.all(),
        to_field_name='id',
        required=False,
        null_option='None',
    )
    tag = TagFilterField(model)


class TrunkEditForm(BootstrapMixin, forms.ModelForm):

    trunk = forms.CharField(
        required=True,
        label="Name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'autocomplete': 'off',
                'pattern': r'^\+?[0-9A-D\*\#]+$',
                'title': 'Enter the Trunk Name'
            }
        )
    )
    tags = DynamicModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        required=False
    )

    class Meta:
        model = Trunk
        fields = ('trunk', 'tenant', 'region', 'description', 'provider', 'destination', 'tags')


class TrunkBulkEditForm(BootstrapMixin, AddRemoveTagsForm, BulkEditForm):

    pk = forms.ModelMultipleChoiceField(
        queryset=Trunk.objects.all(),
        widget=forms.MultipleHiddenInput()
    )
    tenant = DynamicModelChoiceField(
        queryset=Tenant.objects.all(),
        to_field_name='id',
        required=False,
        null_option='None',
    )
    region = DynamicModelChoiceField(
        queryset=Region.objects.all(),
        to_field_name='id',
        required=False,
        null_option='None',
    )
    provider = DynamicModelChoiceField(
        queryset=Provider.objects.all(),
        to_field_name='id',
        required=False,
        null_option='None',
    )
    # Implement plugin API to migrate to DynamicModelChoiceField
    destination = forms.CharField(
        max_length=200,
        required=False
    )
    description = forms.CharField(
        max_length=200,
        required=False
    )

    class Meta:
        nullable_fields = ('region', 'provider', 'destination', 'description')


class TrunkCSVForm(CSVModelForm):
    tenant = CSVModelChoiceField(
        queryset=Tenant.objects.all(),
        required=True,
        to_field_name='name',
        help_text='Assigned tenant'
    )
    provider = CSVModelChoiceField(
        queryset=Provider.objects.all(),
        to_field_name='name',
        required=False,
        help_text='Originating provider'
    )
    region = CSVModelChoiceField(
        queryset=Region.objects.all(),
        required=False,
        to_field_name='name',
        help_text='Assigned region'
    )

    class Meta:
        model = Trunk
        fields = Trunk.csv_headers
        help_texts = {
            'destination': "Destination for SIP Trunk",
        }



class UCClusterFilterForm(BootstrapMixin, forms.Form):

    model = UCCluster
    q = forms.CharField(
        required=False,
        label='Search'
    )
    tenant = DynamicModelMultipleChoiceField(
        queryset=Tenant.objects.all(),
        to_field_name='id',
        required=False,
        null_option='None',
    )

    tag = TagFilterField(model)


class UCClusterEditForm(BootstrapMixin, forms.ModelForm):

    UCCluster = forms.CharField(
        required=True,
        label="Name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'autocomplete': 'off',
                'pattern': r'^\+?[0-9A-D\*\#]+$',
                'title': 'Enter the UCCluster Name'
            }
        )
    )
    tags = DynamicModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        required=False
    )

    class Meta:
        model = UCCluster
        fields = ('uccluster', 'tenant', 'description', 'publisher', 'subscriber1', 'subscriber2', 'subscriber3', 'subscriber4', 'tftp1', 'tftp2')


class UCClusterBulkEditForm(BootstrapMixin, AddRemoveTagsForm, BulkEditForm):

    pk = forms.ModelMultipleChoiceField(
        queryset=UCCluster.objects.all(),
        widget=forms.MultipleHiddenInput()
    )
    tenant = DynamicModelChoiceField(
        queryset=Tenant.objects.all(),
        to_field_name='id',
        required=False,
        null_option='None',
    )
    # Implement plugin API to migrate to DynamicModelChoiceField
    description = forms.CharField(
        max_length=200,
        required=False
    )
    publisher = forms.CharField(
        max_length=200,
        required=False
    )
    subscriber1 = forms.CharField(
        max_length=200,
        required=False
    )
    subscriber2 = forms.CharField(
        max_length=200,
        required=False
    )
    subscriber3 = forms.CharField(
        max_length=200,
        required=False
    )
    subscriber4 = forms.CharField(
        max_length=200,
        required=False
    )
    tftp1 = forms.CharField(
        max_length=200,
        required=False
    )
    tftp2 = forms.CharField(
        max_length=200,
        required=False
    )
    class Meta:
        nullable_fields = ('description', 'subscriber1', 'subscriber2', 'subscriber3', 'subscriber4', 'tftp1', 'tftp2')


class UCClusterCSVForm(CSVModelForm):
    tenant = CSVModelChoiceField(
        queryset=Tenant.objects.all(),
        required=True,
        to_field_name='name',
        help_text='Assigned tenant'
    )

    class Meta:
        model = UCCluster
        fields = UCCluster.csv_headers


class DevicePoolFilterForm(BootstrapMixin, forms.Form):

    model = DevicePool
    q = forms.CharField(
        required=False,
        label='Search'
    )
    tenant = DynamicModelMultipleChoiceField(
        queryset=Tenant.objects.all(),
        to_field_name='id',
        required=False,
        null_option='None',
    )
    region = DynamicModelMultipleChoiceField(
        queryset=Region.objects.all(),
        to_field_name='id',
        required=False,
        null_option='None',
    )
    tag = TagFilterField(model)


class DevicePoolEditForm(BootstrapMixin, forms.ModelForm):

    devicepool = forms.CharField(
        required=True,
        label="Name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'autocomplete': 'off',
                'pattern': r'^\+?[0-9A-D\*\#]+$',
                'title': 'Enter the Device Pool Name'
            }
        )
    )
    tags = DynamicModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        required=False
    )

    class Meta:
        model = DevicePool
        fields = ('devicepool', 'tenant', 'region', 'description', 'datetimegroup', 'localroutegroup', 'cmgroup', 'tags')


class DevicePoolBulkEditForm(BootstrapMixin, AddRemoveTagsForm, BulkEditForm):

    pk = forms.ModelMultipleChoiceField(
        queryset=Trunk.objects.all(),
        widget=forms.MultipleHiddenInput()
    )
    tenant = DynamicModelChoiceField(
        queryset=Tenant.objects.all(),
        to_field_name='id',
        required=False,
        null_option='None',
    )
    region = DynamicModelChoiceField(
        queryset=Region.objects.all(),
        to_field_name='id',
        required=False,
        null_option='None',
    )
    # Implement plugin API to migrate to DynamicModelChoiceField
    datetimegroup = forms.CharField(
        max_length=200,
        required=False
    )
    localroutegroup = forms.CharField(
        max_length=200,
        required=False
    )
    cmgroup = forms.CharField(
        max_length=200,
        required=False
    )
    description = forms.CharField(
        max_length=200,
        required=False
    )

    class Meta:
        nullable_fields = ('region', 'description', 'datetimegroup', 'localroutegroup', 'cmgroup')


class DevicePoolCSVForm(CSVModelForm):
    tenant = CSVModelChoiceField(
        queryset=Tenant.objects.all(),
        required=True,
        to_field_name='name',
        help_text='Assigned tenant'
    )
    region = CSVModelChoiceField(
        queryset=Region.objects.all(),
        required=False,
        to_field_name='name',
        help_text='Assigned region'
    )

    class Meta:
        model = DevicePool
        fields = DevicePool.csv_headers
