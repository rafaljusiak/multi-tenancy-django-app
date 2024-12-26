from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from multi_tenancy_django_app.tenants.models import Tenant
from multi_tenancy_django_app.tenants.serializers import TenantSerializer


class TenantViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    lookup_field = "tenant_id"
    lookup_url_kwarg = "tenant_id"
    permission_classes = (IsAuthenticated,)
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer
