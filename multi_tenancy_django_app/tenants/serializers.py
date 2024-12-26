from rest_framework import serializers

from multi_tenancy_django_app.tenants.models import Tenant


class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = ("tenant_id", "domain")


class BaseTenantRelatedModelSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        tenant = self.context["request"].tenant
        data = {**validated_data, "tenant": tenant}
        return super().create(data)
