from django.http import Http404

from multi_tenancy_django_app.tenants.models import Tenant


class TenantMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            domain = request.get_host().split(":")[0]
            request.tenant = Tenant.objects.get(domain=domain)
        except Tenant.DoesNotExist:
            raise Http404("Tenant not found")

        return self.get_response(request)
