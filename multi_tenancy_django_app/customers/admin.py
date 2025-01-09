from django.contrib import admin

from multi_tenancy_django_app.customers.models import Customer, Organization

admin.site.register(Customer)
admin.site.register(Organization)
