from django.db import models
from django_tenants.models import DomainMixin, TenantMixin


class Tenant(TenantMixin):
    organization = models.ForeignKey("customers.Organization", on_delete=models.CASCADE)

    name = models.CharField(max_length=255)


class Domain(DomainMixin):
    pass
