# Client Project System (Django + MySQL)

## Setup Instructions

### 1. MySQL Setup
```sql
CREATE DATABASE client_project_db;
CREATE USER 'testuser'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON client_project_db.* TO 'testuser'@'localhost';
FLUSH PRIVILEGES;
```

### 2. Install Requirements
```bash
python -m venv venv
# Windows: venv\Scripts\activate
# Linux/Mac: source venv/bin/activate

pip install -r requirements.txt
```

### 3. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### 4. Run Server
```bash
python manage.py runserver
```

### API Endpoints
- GET /api/clients/
- POST /api/clients/
- GET /api/clients/{id}/
- PUT/PATCH /api/clients/{id}/
- DELETE /api/clients/{id}/
- POST /api/clients/{id}/projects/
- GET /api/projects/
