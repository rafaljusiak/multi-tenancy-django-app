from multi_tenancy_django_app.customers.models import Customer, Department, Organization
from multi_tenancy_django_app.tenants.serializers import BaseTenantRelatedModelSerializer


class OrganizationSerializer(BaseTenantRelatedModelSerializer):
    class Meta:
        model = Organization
        fields = ("id", "name")


class DepartmentSerializer(BaseTenantRelatedModelSerializer):
    class Meta:
        model = Department
        fields = ("id", "name")


class CustomerSerializer(BaseTenantRelatedModelSerializer):
    class Meta:
        model = Customer
        fields = ("id", "name")
