from django.http import Http404

from multi_tenancy_django_app.tenants.models import Tenant


class TenantMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            request.tenant = self.get_tenant_from_header(
                request
            ) or self.get_tenant_from_host(request)
        except Tenant.DoesNotExist:
            raise Http404("Tenant not found")

        return self.get_response(request)

    def get_tenant_from_header(self, request) -> Tenant | None:
        if tenant_id := request.headers.get("X-Tenant-ID"):
            return Tenant.objects.get(tenant_id=tenant_id)

    def get_tenant_from_host(self, request) -> Tenant:
        tenant_domain = request.get_host().split(":")[0]
        return Tenant.objects.get(domain=tenant_domain)
