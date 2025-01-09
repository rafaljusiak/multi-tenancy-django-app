from django.contrib import admin

from multi_tenancy_django_app.admin.admin import TenantModelAdmin
from multi_tenancy_django_app.resources.models import Resource


@admin.register(Resource)
class ResourceAdmin(TenantModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        print(qs)
        return qs
