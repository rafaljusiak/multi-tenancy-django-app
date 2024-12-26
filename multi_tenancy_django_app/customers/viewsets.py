from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from multi_tenancy_django_app.customers.models import Customer, Department, Organization
from multi_tenancy_django_app.customers.serializers import (
    CustomerSerializer,
    DepartmentSerializer,
    OrganizationSerializer,
)
from multi_tenancy_django_app.tenants.managers import TenantBasedQuerySet


class BaseTenantBasedViewSet(viewsets.GenericViewSet):
    queryset: TenantBasedQuerySet

    def get_queryset(self):
        return super().get_queryset().for_tenant(self.request.tenant)


class OrganizationViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    BaseTenantBasedViewSet,
):
    permission_classes = (IsAuthenticated,)
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class DepartmentViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    BaseTenantBasedViewSet,
):
    permission_classes = (IsAuthenticated,)
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class CustomerViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    BaseTenantBasedViewSet,
):
    permission_classes = (IsAuthenticated,)
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
