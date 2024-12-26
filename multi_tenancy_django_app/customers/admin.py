from django.contrib import admin

from multi_tenancy_django_app.customers.models import Customer, Department, Organization

admin.site.register(Customer)
admin.site.register(Department)
admin.site.register(Organization)
