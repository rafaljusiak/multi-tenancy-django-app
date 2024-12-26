from django.contrib import admin

from multi_tenancy_django_app.tenants.models import Tenant

admin.site.register(Tenant)
