import uuid

from rest_framework.reverse import reverse

from multi_tenancy_django_app.tenants.models import Tenant


def test_tenant_list(rest_client, tenant_a: Tenant, tenant_b: Tenant):
    response = rest_client.get(reverse("api:tenants-list"))
    assert response.status_code == 200
    assert len(response.json()) == 2


def test_tenant_retrieve(rest_client, tenant_a: Tenant):
    response = rest_client.get(
        reverse("api:tenants-detail", args=(tenant_a.tenant_id,))
    )
    assert response.status_code == 200
    assert response.json()["tenant_id"] == tenant_a.tenant_id


def test_tenant_create(rest_client, tenant_a: Tenant):
    data = {"tenant_id": str(uuid.uuid4()), "domain": "c.com"}
    response = rest_client.post(reverse("api:tenants-list"), data=data)
    assert response.status_code == 201


def test_tenant_cannot_be_deleted(rest_client, tenant_a: Tenant):
    response = rest_client.delete(
        reverse("api:tenants-detail", args=(tenant_a.tenant_id,))
    )
    assert response.status_code == 405


def test_tenant_cannot_be_updated(rest_client, tenant_a: Tenant):
    data = {"tenant_id": str(uuid.uuid4()), "domain": "c.com"}
    response = rest_client.put(reverse("api:tenants-detail", args=(tenant_a.tenant_id,)), data=data)
    assert response.status_code == 405
