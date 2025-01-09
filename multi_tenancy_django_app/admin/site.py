from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html


class AdminSite(admin.AdminSite):
    site_header = "Multi Tenant Admin"
    index_template = "admin/base.override.html"

    def each_context(self, request):
        context = super().each_context(request)
        context["tenant_button"] = format_html(
            '<a class="button" href="{}">Select Tenant</a>',
            reverse("select_tenant_admin"),
        )
        return context
