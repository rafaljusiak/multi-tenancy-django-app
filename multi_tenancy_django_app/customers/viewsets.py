from rest_framework import mixins

from multi_tenancy_django_app.customers.models import Customer, Department, Organization
from multi_tenancy_django_app.customers.serializers import (
    CustomerSerializer,
    DepartmentSerializer,
    OrganizationSerializer,
)
from multi_tenancy_django_app.tenants.viewsets import BaseTenantRelatedViewSet


class OrganizationViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    BaseTenantRelatedViewSet,
):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class DepartmentViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    BaseTenantRelatedViewSet,
):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class CustomerViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    BaseTenantRelatedViewSet,
):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
