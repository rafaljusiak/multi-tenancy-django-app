from __future__ import annotations

import abc
from typing import TYPE_CHECKING

from django.db import models

if TYPE_CHECKING:
    from multi_tenancy_django_app.tenants.models import Tenant


class TenantBasedQuerySet(abc.ABC, models.QuerySet):
    @abc.abstractmethod
    def for_tenant(self, tenant: Tenant):
        pass
