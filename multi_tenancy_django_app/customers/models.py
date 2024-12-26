from django.db import models

from multi_tenancy_django_app.customers.managers import (
    OrganizationManager,
    DepartmentManager,
    CustomerManager,
)


class Organization(models.Model):
    tenant = models.ForeignKey("tenants.Tenant", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    objects = OrganizationManager


class Department(models.Model):
    organization = models.ForeignKey("customers.Organization", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    objects = DepartmentManager


class Customer(models.Model):
    department = models.ForeignKey("customers.Department", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    objects = CustomerManager
