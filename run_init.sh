#docker compose build --no-cache
docker compose run --rm django python manage.py shell -c "
from django.contrib.auth.models import User;from multi_tenancy_django_app.tenants.models import Tenant;
User.objects.filter(username='admin').first() or User.objects.create_superuser('admin', 'admin@example.com', 'password');
Tenant.objects.get_or_create(domain='0.0.0.0')
"
