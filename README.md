# Multi-tenancy Django App

## Overview

This application is designed for multi-tenant scenarios using a **shared database and shared schema** architecture. 

### Architecture Overview

- **Shared Database and Schema**:  
  All tenants use a single database and schema. The `Tenant` table acts as the central point, with all other tables 
  containing a foreign key to the tenant. This ensures data isolation at the application level.

- **Core Components**:
  1. `TenantMiddleware`:
      - Identifies the current tenant based on the `X-Tenant-ID` header or domain name.
      - Returns a 404 if the tenant does not exist in the database.
  2. Base Classes:
      - `TenantRelatedModel`: Ensures all models are linked to a tenant.
      - `BaseTenantRelatedViewSet`: Automatically filters data based on the tenant.
      - `BaseTenantRelatedModelSerializer`: Handles tenant-related serialization logic.

## Setup Instructions

### Prerequisites

- Ensure Docker is installed on your system.

### Steps to Set Up the Application

1. Clone the repository:
```
git clone https://github.com/your-repo/multi-tenancy-django-app.git
cd multi-tenancy-django-app
```

2. Initialize the application:
```
./run_init.sh
```

3. Start the application:
```
./run_app.sh
```

4. Access the application:
   - Default: http://0.0.0.0:8000

### Running Tests

To run the test suite, execute the following command:
```
./run_tests.sh
```

## Examples of Interaction

### CRUD and Admin Panel

The admin panel is accessible via the URL: http://0.0.0.0:8000/admin

**Login credentials**:
   - Username: `admin`  
   - Password: `P@ssw0rd`

### Example API Request

Create a token in the admin panel at the following URL: http://0.0.0.0:8000/admin/authtoken/tokenproxy/add/  
Include it in the `Authorization` header as `Token <your-token>`. Example:

```
curl -X POST http://0.0.0.0:8000/api/organizations/ \
   -H "Content-Type: application/json" \
   -H "Authorization: Token <your-token>"
   -d '{"name": "New Organization"}'
```
