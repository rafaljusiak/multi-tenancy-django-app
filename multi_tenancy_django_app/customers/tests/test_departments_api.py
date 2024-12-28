from rest_framework.reverse import reverse

from multi_tenancy_django_app.customers.models import Department


def test_departments_list(rest_client, department_a, department_b):
    response = rest_client.get(reverse("api:departments-list"))
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["id"] == department_a.id


def test_departments_detail(rest_client, department_a, department_b):
    response = rest_client.get(
        reverse("api:departments-detail", args=(department_a.id,))
    )
    assert response.status_code == 200
    assert response.json()["id"] == department_a.id


def test_departments_detail_cannot_access_another_tenant(
    rest_client, department_a, department_b
):
    response = rest_client.get(
        reverse("api:departments-detail", args=(department_b.id,))
    )
    assert response.status_code == 404


def test_departments_create(rest_client, organization_a):
    data = {"name": "test department", "organization": organization_a.id}
    response = rest_client.post(reverse("api:departments-list"), data)
    assert response.status_code == 201

    departments = Department.objects.all()
    assert departments.count() == 1

    department = departments.first()
    assert department.name == "test department"
    assert department.organization.id == organization_a.id


def test_cannot_create_department_without_organization(rest_client, organization_a):
    data = {"name": "test department"}
    response = rest_client.post(reverse("api:departments-list"), data)
    assert response.status_code == 400


def test_department_cannot_be_deleted(rest_client, department_a):
    response = rest_client.delete(
        reverse("api:departments-detail", args=(department_a.id,))
    )
    assert response.status_code == 405


def test_unauthorized_user_cannot_list_departments(
    unauthorized_rest_client, department_a, department_b
):
    response = unauthorized_rest_client.get(reverse("api:departments-list"))
    assert response.status_code == 401


def test_unauthorized_user_cannot_create_departments(
    unauthorized_rest_client, organization_a
):
    data = {"name": "test department", "organization": organization_a.id}
    response = unauthorized_rest_client.post(reverse("api:departments-list"), data)
    assert response.status_code == 401
