import uuid

from django.db import models


class Tenant(models.Model):
    tenant_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    domain = models.CharField(max_length=255, unique=True)
