#!/bin/bash

GREEN='\033[0;32m'
NC='\033[0m'

echo -e "${GREEN}Building Docker containers...${NC}"
echo
docker compose build --no-cache
echo
echo -e "${GREEN}Docker containers built successfully!${NC}"
echo

echo -e "${GREEN}Running database migrations and creating superuser and default tenant...${NC}"
echo
docker compose up -d django
docker compose exec django python manage.py migrate
docker compose exec django python manage.py shell -c "
from django.contrib.auth.models import User;
from multi_tenancy_django_app.tenants.models import Tenant;
User.objects.filter(username='admin').first() or User.objects.create_superuser('admin', 'admin@example.com', 'P@ssw0rd');
Tenant.objects.get_or_create(domain='0.0.0.0')
"
docker compose stop
echo
echo -e "${GREEN}Done!${NC}"
echo
