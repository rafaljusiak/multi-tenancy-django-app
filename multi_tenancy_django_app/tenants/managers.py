from __future__ import annotations

from typing import TYPE_CHECKING

from django.db import models

if TYPE_CHECKING:
    from multi_tenancy_django_app.tenants.models import Tenant


class TenantRelatedQuerySet(models.QuerySet):
    def for_tenant(self, tenant: Tenant):
        return self.filter(tenant=tenant)
