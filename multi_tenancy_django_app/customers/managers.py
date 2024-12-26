from multi_tenancy_django_app.common.managers import TenantBasedQuerySet
from multi_tenancy_django_app.tenants.models import Tenant


class OrganizationQuerySet(TenantBasedQuerySet):
    def for_tenant(self, tenant: Tenant):
        return self.filter(tenant=tenant)


OrganizationManager = OrganizationQuerySet.as_manager()


class DepartmentQuerySet(TenantBasedQuerySet):
    def for_tenant(self, tenant: Tenant):
        return self.filter(organization__tenant=tenant)


DepartmentManager = DepartmentQuerySet.as_manager()


class CustomerQuerySet(TenantBasedQuerySet):
    def for_tenant(self, tenant: Tenant):
        return self.filter(department__organization__tenant=tenant)


CustomerManager = CustomerQuerySet.as_manager()
