from django.contrib import admin
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from multi_tenancy_django_app.admin.admin import SelectTenantAdminView

router = DefaultRouter()

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "select-tenant/",
        staff_member_required(SelectTenantAdminView.as_view()),
        name="select_tenant_admin",
    ),
    path("api/", include((router.urls, "api"))),
]
