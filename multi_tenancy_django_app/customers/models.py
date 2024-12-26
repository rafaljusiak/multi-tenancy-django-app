from django.db import models

from multi_tenancy_django_app.tenants.models import TenantRelatedModel


class Organization(TenantRelatedModel):
    tenant = models.ForeignKey("tenants.Tenant", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)


class Department(TenantRelatedModel):
    organization = models.ForeignKey("customers.Organization", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)


class Customer(TenantRelatedModel):
    department = models.ForeignKey("customers.Department", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
