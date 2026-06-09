# 🎓 Cloud-Based NAAC Data Management & Accreditation Support System

![React](https://img.shields.io/badge/React-19-61DAFB?logo=react)
![Django](https://img.shields.io/badge/Django-REST%20Framework-092E20?logo=django)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?logo=postgresql)
![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker)
![Keycloak](https://img.shields.io/badge/Keycloak-Authentication-EF4444)


A **centralized, secure, and cloud-ready platform** designed to streamline **NAAC accreditation data management** for higher education institutions. The system enables efficient document storage, role-based access control, OCR-powered search, analytics dashboards, audit logging, and automated report generation to simplify accreditation workflows.

---

## 🚀 Key Features

### 🔐 Authentication & Authorization

* Keycloak-based Single Sign-On (SSO)
* OIDC/JWT authentication
* Role-Based Access Control (RBAC)
* Multi-role support:

  * IQAC Admin
  * Department Admin
  * Faculty
  * Student

### 📁 Document Management

* Secure document uploads
* Version control support
* Department-wise organization
* Criteria-wise evidence storage
* Cloud object storage using MinIO

### 🔍 Intelligent Search & Retrieval

* OCR-powered text extraction
* Full-text document indexing
* Fast search with Meilisearch
* Metadata-based filtering

### 📊 Analytics & Dashboards

* Embedded Metabase dashboards
* Accreditation progress tracking
* Department performance analytics
* Institutional insights and reports

### 📄 Automated Report Generation

* Criterion-wise NAAC reports
* Downloadable PDF reports
* Evidence compilation support
* Accreditation-ready documentation

### 📝 Audit Logging

* Comprehensive user activity tracking
* Document access monitoring
* System-wide audit trails
* Compliance and accountability support

---

## 🏗️ System Architecture

```text
┌─────────────────┐
│   React Frontend │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Django REST API │
└───────┬─────────┘
        │
 ┌──────┼─────────────┬────────────┬───────────┐
 ▼      ▼             ▼            ▼
PostgreSQL   Keycloak   Meilisearch   MinIO
(Database)   (Auth)      (Search)   (Storage)
                    │
                    ▼
               Metabase
              (Analytics)
```

---

## 🛠️ Tech Stack

| Category         | Technology                    |
| ---------------- | ----------------------------- |
| Frontend         | React.js, Vite, Bootstrap     |
| Backend          | Django, Django REST Framework |
| Database         | PostgreSQL                    |
| Authentication   | Keycloak (OIDC/JWT)           |
| Object Storage   | MinIO                         |
| Search Engine    | Meilisearch                   |
| OCR Processing   | Tesseract OCR                 |
| Analytics        | Metabase                      |
| Containerization | Docker, Docker Compose        |
| Version Control  | Git & GitHub                  |

---

## 📂 Project Structure

```bash
naac-data-management-system/
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
├── backend/
│   ├── api/
│   ├── documents/
│   ├── reports/
│   ├── users/
│   └── manage.py
│
├── docker/
├── docs/
├── uploads/
├── docker-compose.yml
├── .env.example
└── README.md
```

---

## ⚙️ Prerequisites

Before running the project, ensure the following are installed:

* Docker
* Docker Compose
* Git

Verify installation:

```bash
docker --version
docker-compose --version
git --version
```

---

## 🚀 Quick Start

### 1. Clone Repository

```bash
git clone <repository-url>
cd naac-data-management-system
```

### 2. Configure Environment Variables

```bash
cp .env.example .env
```

Update the `.env` file with your required configurations.

---

### 3. Start All Services

```bash
docker-compose up --build
```

---

### 4. Apply Database Migrations

Open a new terminal:

```bash
docker-compose exec backend python manage.py migrate
```

---

### 5. Create Admin User

```bash
docker-compose exec backend python manage.py createsuperuser
```

---

### 6. Configure Keycloak

Open:

```text
http://localhost:8080
```

Default credentials:

```text
Username: admin
Password: admin
```

Import:

```text
keycloak-realm-config.json
```

---

### 7. Configure Metabase

Open:

```text
http://localhost:3000
```

Connect Metabase to PostgreSQL and create analytics dashboards.

---

## 🌐 Application URLs

| Service       | URL                   |
| ------------- | --------------------- |
| Frontend      | http://localhost:3000 |
| Backend API   | http://localhost:8000 |
| Keycloak      | http://localhost:8080 |
| MinIO Console | http://localhost:9001 |
| Meilisearch   | http://localhost:7700 |
| Metabase      | http://localhost:3000 |

---

## 📚 API Endpoints

### Authentication

```http
POST /api/auth/login/
```

### Documents

```http
GET /api/documents/criteria/
POST /api/documents/upload/
GET /api/documents/search/?q=<query>
```

### Reports

```http
GET /api/reports/naac/<criteria>/
```

---

## 💻 Local Development

### Backend Setup

```bash
cd backend

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
```

---

### Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

---

## 🔒 Security Features

* JWT Authentication
* Role-Based Access Control
* Secure Document Storage
* Audit Logging
* Access Tracking
* API Protection
* Cloud Storage Integration

---

## ☁️ Production Deployment

For production environments:

### Infrastructure Recommendations

* AWS RDS for PostgreSQL
* AWS S3 for Object Storage
* NGINX Reverse Proxy
* SSL/TLS Certificates
* Monitoring & Logging
* Automated Backups

### Deployment Checklist

* Configure production environment variables
* Enable HTTPS
* Set up database backups
* Configure monitoring
* Enable centralized logging
* Harden security settings

---

## 🎯 Future Enhancements

* AI-powered accreditation recommendations
* Advanced analytics and forecasting
* Mobile application support
* Multi-institution deployment
* Workflow automation
* Email and notification services
* Document approval workflows
* Accreditation score prediction

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature-name
```

3. Commit changes

```bash
git commit -m "Add new feature"
```

4. Push to branch

```bash
git push origin feature-name
```

5. Create a Pull Request

---

## 👨‍💻 Authors

**Sohan D Souza**

* Full Stack Developer
* AI/ML Enthusiast
* Salesforce Developer

---


---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub. It helps increase visibility and supports future development.

### GitHub Topics

```text
naac
naac-accreditation
education-technology
document-management
react
vite
django
django-rest-framework
postgresql
docker
keycloak
jwt-authentication
minio
meilisearch
ocr
metabase
analytics-dashboard
role-based-access-control
full-stack-development
cloud-computing
```
