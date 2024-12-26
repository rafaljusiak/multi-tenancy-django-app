import uuid

from django.db import models

from multi_tenancy_django_app.tenants.managers import TenantBasedQuerySet


class TenantRelatedModel(models.Model):
    tenant = models.ForeignKey("tenants.Tenant", on_delete=models.CASCADE)

    objects = TenantBasedQuerySet.as_manager()

    class Meta:
        abstract = True


class Tenant(models.Model):
    tenant_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    domain = models.CharField(max_length=255, unique=True)
