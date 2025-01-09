from django import forms
from django.contrib import admin
from django.contrib.admin.options import csrf_protect_m
from django.urls import reverse
from django.views.generic import FormView
from django_tenants.utils import tenant_context

from multi_tenancy_django_app.tenants.models import Tenant


class SelectTenantForm(forms.Form):
    tenant = forms.ModelChoiceField(queryset=Tenant.objects.all())


class SelectTenantAdminView(FormView):
    form_class = SelectTenantForm
    template_name = "admin/select_tenant.html"

    def form_valid(self, form):
        tenant_id = form.cleaned_data["tenant"].id
        self.request.session["tenant_id"] = tenant_id
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("admin:index")


class TenantModelAdmin(admin.ModelAdmin):
    def get_object(self, request, object_id, from_field=None):
        with tenant_context(self._get_tenant_from_session(request)):
            return super().get_object(request, object_id, from_field)

    @csrf_protect_m
    def changelist_view(self, request, extra_context=None):
        with tenant_context(self._get_tenant_from_session(request)):
            return super().changelist_view(request, extra_context)

    def _get_tenant_from_session(self, request) -> Tenant:
        if request.user.is_superuser and "tenant_id" in request.session:
            tenant_id = request.session["tenant_id"]
            tenant = Tenant.objects.get(id=tenant_id)
        else:
            tenant = request.tenant

        return tenant
