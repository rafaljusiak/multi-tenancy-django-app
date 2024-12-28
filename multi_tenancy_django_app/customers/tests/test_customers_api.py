from rest_framework.reverse import reverse

from multi_tenancy_django_app.customers.models import Customer


def test_customers_list(rest_client, customer_a, customer_b):
    response = rest_client.get(reverse("api:customers-list"))
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["id"] == customer_a.id


def test_customers_detail(rest_client, customer_a, customer_b):
    response = rest_client.get(reverse("api:customers-detail", args=(customer_a.id,)))
    assert response.status_code == 200
    assert response.json()["id"] == customer_a.id


def test_customers_detail_cannot_access_another_tenant(
    rest_client, customer_a, customer_b
):
    response = rest_client.get(reverse("api:customers-detail", args=(customer_b.id,)))
    assert response.status_code == 404


def test_customers_create(rest_client, department_a):
    data = {"name": "test customer", "department": department_a.id}
    response = rest_client.post(reverse("api:customers-list"), data)
    assert response.status_code == 201

    customers = Customer.objects.all()
    assert customers.count() == 1

    customer = customers.first()
    assert customer.name == "test customer"
    assert customer.department.id == department_a.id


def test_cannot_create_customer_without_department(rest_client, organization_a):
    data = {"name": "test customer"}
    response = rest_client.post(reverse("api:customers-list"), data)
    assert response.status_code == 400


def test_customer_cannot_be_deleted(rest_client, customer_a):
    response = rest_client.delete(
        reverse("api:customers-detail", args=(customer_a.id,))
    )
    assert response.status_code == 405


def test_unauthorized_user_cannot_list_customers(
    unauthorized_rest_client, customer_a, customer_b
):
    response = unauthorized_rest_client.get(reverse("api:customers-list"))
    assert response.status_code == 401


def test_unauthorized_user_cannot_create_customers(
    unauthorized_rest_client, department_a
):
    data = {"name": "test customer", "department": department_a.id}
    response = unauthorized_rest_client.post(reverse("api:customers-list"), data)
    assert response.status_code == 401
