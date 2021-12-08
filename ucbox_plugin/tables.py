import django_tables2 as tables
from .models import Number, Trunk, UCCluster, DevicePool
from utilities.tables import BaseTable, ToggleColumn


class NumberTable(BaseTable):

    pk = ToggleColumn()
    number = tables.LinkColumn()
    tenant = tables.LinkColumn()
    region = tables.LinkColumn()
    provider = tables.LinkColumn()
    forward_to = tables.LinkColumn()

    class Meta(BaseTable.Meta):
        model = Number
        fields = ('pk', 'number', 'tenant', 'region', 'description', 'provider', 'forward_to')

class TrunkTable(BaseTable):

    pk = ToggleColumn()
    trunk = tables.LinkColumn()
    tenant = tables.LinkColumn()
    destination = tables.LinkColumn()
    region = tables.LinkColumn()
    provider = tables.LinkColumn()

    class Meta(BaseTable.Meta):
        model = Trunk
        fields = ('pk', 'trunk', 'tenant', 'destination', 'region', 'provider', 'description')


class UCClusterTable(BaseTable):

    pk = ToggleColumn()
    uccluster = tables.LinkColumn()
    tenant = tables.LinkColumn()
    description = tables.LinkColumn()
    publisher = tables.LinkColumn()
    subscriber1 = tables.LinkColumn()
    subscriber2 = tables.LinkColumn()
    subscriber3 = tables.LinkColumn()
    subscriber4 = tables.LinkColumn()
    tftp1 = tables.LinkColumn()
    tftp2 = tables.LinkColumn()

    class Meta(BaseTable.Meta):
        model = UCCluster
        fields = ('pk', 'uccluster', 'tenant', 'description', 'publisher', 'subscriber1', 'subscriber2', 'subscriber3', 'subscriber4', 'tftp1', 'tftp2')

class DevicePoolTable(BaseTable):

    pk = ToggleColumn()
    devicepool = tables.LinkColumn()
    tenant = tables.LinkColumn()
    description = tables.LinkColumn()
    region = tables.LinkColumn()
    datetimegroup = tables.LinkColumn()
    localroutegroup = tables.LinkColumn()
    cmgroup = tables.LinkColumn()
    class Meta(BaseTable.Meta):
        model = DevicePool
        fields = ('pk', 'devicepool', 'tenant', 'description', 'region', 'datetimegroup', 'localroutegroup', 'cmgroup')
