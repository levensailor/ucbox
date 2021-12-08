from django.db import models
from extras.models import TaggedItem
from netbox.models import ChangeLoggedModel
from utilities.querysets import RestrictedQuerySet
from django.core.validators import RegexValidator
from taggit.managers import TaggableManager
from django.urls import reverse

number_validator = RegexValidator(
    r"^\+?[0-9A-D\#\*]*$",
    "Numbers can only contain: leading +, digits 0-9; chars A, B, C, D; # and *"
)

class Trunk(ChangeLoggedModel):
    trunk = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    tags = TaggableManager(through=TaggedItem)
    tenant = models.ForeignKey(
        to='tenancy.Tenant',
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )
    provider = models.ForeignKey(
        to="circuits.Provider",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="trunk_provider_set"
    )
    region = models.ForeignKey(
        to="dcim.Region",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="trunk_region_set"
    )
    objects = RestrictedQuerySet.as_manager()

    csv_headers = ['trunk', 'destination', 'description', 'tenant', 'provider', 'region']

    def __str__(self):
        return str(self.trunk)

    def get_absolute_url(self):
        return reverse("plugins:ucbox_plugin:trunk_view", kwargs={"pk": self.pk})

    class Meta:
        unique_together = ("trunk", "tenant",)#ermoe enant here

class Number(ChangeLoggedModel):
    """A Number represents a single telephone number of an arbitrary format.
    A Number can contain only valid DTMF characters and leading plus sign for E.164 support:
      - leading plus ("+") sign (optional)
      - digits 0-9
      - characters A, B, C, D
      - pound sign ("#")
      - asterisk sign ("*")
    Digit delimiters are now allowed. They will be implemented as a separate output formatter function.
    Number values can be not unique.
    Tenant is a mandatory option representing a number partition. Number and Tenant are globally unique.
    A Number can optionally be assigned with Provider and Region relations.
    A Number can contain an optional Description.
    A Number can optionally be tagged with Tags.
    """

    number = models.CharField(max_length=32, validators=[number_validator])
    tenant = models.ForeignKey(
        to='tenancy.Tenant',
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )
    description = models.CharField(max_length=200, blank=True)
    provider = models.ForeignKey(
        to="circuits.Provider",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="number_provider_set"
    )
    region = models.ForeignKey(
        to="dcim.Region",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="number_region_set"
    )
    forward_to = models.ForeignKey(
        to="self",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="forward_to_set"
    )
    tags = TaggableManager(through=TaggedItem)

    objects = RestrictedQuerySet.as_manager()

    csv_headers = ['number', 'tenant', 'region', 'description', 'provider', 'forward_to']

    def __str__(self):
        return str(self.number)

    def get_absolute_url(self):
        return reverse("plugins:ucbox_plugin:number_view", kwargs={"pk": self.pk})

    class Meta:
        unique_together = ("number", "tenant",)#ermoe enant here


class UCCluster(ChangeLoggedModel):
    uccluster = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    tags = TaggableManager(through=TaggedItem)
    tenant = models.ForeignKey(
        to='tenancy.Tenant',
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )
    publisher = models.CharField(max_length=200)
    subscriber1 = models.CharField(max_length=200)
    subscriber2 = models.CharField(max_length=200)
    subscriber3 = models.CharField(max_length=200)
    subscriber4 = models.CharField(max_length=200)
    tftp1 = models.CharField(max_length=200)
    tftp2 = models.CharField(max_length=200)

    objects = RestrictedQuerySet.as_manager()

    csv_headers = ['uccluster', 'tenant', 'description', 'publisher', 'subscriber1', 'subscriber2', 'subscriber3', 'subscriber4', 'tftp1', 'tftp2']

    def __str__(self):
        return str(self.uccluster)

    def get_absolute_url(self):
        return reverse("plugins:ucbox_plugin:uccluster_view", kwargs={"pk": self.pk})

    class Meta:
        unique_together = ("uccluster", "tenant",)#ermoe enant here



class DevicePool(ChangeLoggedModel):
    devicepool = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    tags = TaggableManager(through=TaggedItem)
    tenant = models.ForeignKey(
        to='tenancy.Tenant',
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )
    region = models.ForeignKey(
        to="dcim.Region",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="devicepool_region_set"
    )
    datetimegroup = models.CharField(max_length=200)
    localroutegroup = models.CharField(max_length=200)
    cmgroup = models.CharField(max_length=200)
    objects = RestrictedQuerySet.as_manager()

    csv_headers = ['devicepool', 'tenant', 'description', 'region', 'datetimegroup', 'localroutegroup', 'cmgroup']

    def __str__(self):
        return str(self.devicepool)

    def get_absolute_url(self):
        return reverse("plugins:ucbox_plugin:devicepool_view", kwargs={"pk": self.pk})

    class Meta:
        unique_together = ("devicepool", "tenant",)#ermoe enant here