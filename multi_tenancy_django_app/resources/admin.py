from django.contrib import admin

from multi_tenancy_django_app.resources.models import Resource


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    pass
