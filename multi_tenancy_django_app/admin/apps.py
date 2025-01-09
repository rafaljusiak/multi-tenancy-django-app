from django.contrib.admin.apps import AdminConfig as DjangoAdminConfig


class AdminConfig(DjangoAdminConfig):
    default_site = "multi_tenancy_django_app.admin.site.AdminSite"
