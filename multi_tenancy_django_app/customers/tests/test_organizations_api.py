from rest_framework.reverse import reverse

from multi_tenancy_django_app.customers.models import Organization


def test_organizations_list(rest_client, organization_a, organization_b):
    response = rest_client.get(reverse("api:organizations-list"))
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["id"] == organization_a.id


def test_organizations_detail(rest_client, organization_a, organization_b):
    response = rest_client.get(
        reverse("api:organizations-detail", args=(organization_a.id,))
    )
    assert response.status_code == 200
    assert response.json()["id"] == organization_a.id


def test_organizations_detail_cannot_access_another_tenant(
    rest_client, organization_a, organization_b
):
    response = rest_client.get(
        reverse("api:organizations-detail", args=(organization_b.id,))
    )
    assert response.status_code == 404


def test_organizations_create(rest_client, tenant_a):
    data = {"name": "test name"}
    response = rest_client.post(reverse("api:organizations-list"), data)
    assert response.status_code == 201

    organizations = Organization.objects.all()
    assert organizations.count() == 1

    organization = organizations.first()
    assert organization.name == "test name"
    assert str(organization.tenant_id) == str(tenant_a.tenant_id)


def test_organization_cannot_be_deleted(rest_client, organization_a):
    response = rest_client.delete(
        reverse("api:organizations-detail", args=(organization_a.id,))
    )
    assert response.status_code == 405


def test_unauthorized_user_cannot_list_organizations(
    unauthorized_rest_client, organization_a, organization_b
):
    response = unauthorized_rest_client.get(reverse("api:organizations-list"))
    assert response.status_code == 401


def test_unauthorized_user_cannot_create_organizations(
    unauthorized_rest_client, tenant_a
):
    data = {"name": "test name"}
    response = unauthorized_rest_client.post(reverse("api:organizations-list"), data)
    assert response.status_code == 401
