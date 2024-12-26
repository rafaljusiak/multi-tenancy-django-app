import uuid

import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient

from multi_tenancy_django_app.tenants.models import Tenant


@pytest.fixture
def main_tenant_id():
    return str(uuid.uuid4())


@pytest.fixture
def user(db):
    return User.objects.create_user(
        username="testuser",
        email="testuser@example.com",
        password="P@ssw0rd",
    )


@pytest.fixture
def rest_client(user: User, main_tenant_id) -> APIClient:
    client = APIClient()
    client.force_login(user)
    client.credentials(HTTP_X_TENANT_ID=main_tenant_id)
    return client


@pytest.fixture
def tenant_a(db, main_tenant_id):
    return Tenant.objects.create(domain="a.com", tenant_id=main_tenant_id)


@pytest.fixture
def tenant_b(db):
    return Tenant.objects.create(domain="b.com", tenant_id=uuid.uuid4())
