from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter

from multi_tenancy_django_app.customers.viewsets import (
    OrganizationViewSet,
    DepartmentViewSet,
    CustomerViewSet,
)
from multi_tenancy_django_app.tenants.viewsets import TenantViewSet

router = DefaultRouter()
router.register("tenants", TenantViewSet, basename="tenants")
router.register("organizations", OrganizationViewSet, basename="organizations")
router.register("departments", DepartmentViewSet, basename="departments")
router.register("customers", CustomerViewSet, basename="customers")

urlpatterns = [
    path("admin/", admin.site.urls),
] + router.urls
