<div align="center">

# 🎓 NAAC Data Management & Accreditation Support System

### A centralized, secure, cloud-ready platform for streamlining NAAC accreditation workflows

[![React](https://img.shields.io/badge/React-19-61DAFB?style=for-the-badge&logo=react&logoColor=white)](#)
[![Django](https://img.shields.io/badge/Django-REST%20Framework-092E20?style=for-the-badge&logo=django&logoColor=white)](#)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)](#)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](#)
[![Keycloak](https://img.shields.io/badge/Keycloak-Auth-EF4444?style=for-the-badge&logo=keycloak&logoColor=white)](#)

[![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](#)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?style=flat-square)](#-contributing)
[![Made with ❤](https://img.shields.io/badge/Made%20with-%E2%9D%A4-ff69b4?style=flat-square)](#)

<br>

Document storage&nbsp;•&nbsp;Role-based access&nbsp;•&nbsp;OCR-powered search&nbsp;•&nbsp;Analytics dashboards&nbsp;•&nbsp;Audit logging&nbsp;•&nbsp;Automated reports

</div>

---

## 📑 Table of Contents

- [Key Features](#-key-features)
- [System Architecture](#️-system-architecture)
- [Tech Stack](#️-tech-stack)
- [Project Structure](#-project-structure)
- [Quick Start](#-quick-start)
- [Application URLs](#-application-urls)
- [API Endpoints](#-api-endpoints)
- [Local Development](#-local-development)
- [Security Features](#-security-features)
- [Production Deployment](#️-production-deployment)
- [Future Enhancements](#-future-enhancements)
- [Contributing](#-contributing)
- [Author](#-author)

---

## ✨ Key Features

<table>
<tr>
<td width="50%" valign="top">

### 🔐 Authentication & Authorization
- Keycloak-based Single Sign-On (SSO)
- OIDC / JWT authentication
- Role-Based Access Control (RBAC)
- Multi-role support:
  - 🧑‍💼 IQAC Admin
  - 🏢 Department Admin
  - 👨‍🏫 Faculty
  - 🎓 Student

</td>
<td width="50%" valign="top">

### 📁 Document Management
- Secure document uploads
- Version control support
- Department-wise organization
- Criteria-wise evidence storage
- Cloud object storage via MinIO

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 🔍 Intelligent Search & Retrieval
- OCR-powered text extraction
- Full-text document indexing
- Fast search with Meilisearch
- Metadata-based filtering

</td>
<td width="50%" valign="top">

### 📊 Analytics & Dashboards
- Embedded Metabase dashboards
- Accreditation progress tracking
- Department performance analytics
- Institutional insights & reports

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 📄 Automated Report Generation
- Criterion-wise NAAC reports
- Downloadable PDF reports
- Evidence compilation support
- Accreditation-ready documentation

</td>
<td width="50%" valign="top">

### 📝 Audit Logging
- Comprehensive user activity tracking
- Document access monitoring
- System-wide audit trails
- Compliance & accountability support

</td>
</tr>
</table>

---

## 🏗️ System Architecture

```text
                     ┌──────────────────────┐
                     │     React Frontend    │
                     └──────────┬───────────┘
                                │
                                ▼
                     ┌──────────────────────┐
                     │   Django REST API     │
                     └──────────┬───────────┘
                                │
        ┌───────────┬──────────┼──────────────┬─────────────┐
        ▼            ▼          ▼              ▼             
┌───────────────┐ ┌────────┐ ┌────────────┐ ┌────────┐       
│  PostgreSQL    │ │Keycloak│ │Meilisearch │ │ MinIO  │       
│  (Database)    │ │ (Auth) │ │ (Search)   │ │(Storage)│      
└───────────────┘ └────────┘ └─────┬──────┘ └────────┘       
                                    │
                                    ▼
                              ┌──────────┐
                              │ Metabase │
                              │(Analytics)│
                              └──────────┘
```

---

## 🛠️ Tech Stack

<div align="center">

| Layer | Technology |
|:---|:---|
| 🖥️ **Frontend** | React.js · Vite · Bootstrap |
| ⚙️ **Backend** | Django · Django REST Framework |
| 🗄️ **Database** | PostgreSQL |
| 🔐 **Authentication** | Keycloak (OIDC / JWT) |
| 📦 **Object Storage** | MinIO |
| 🔎 **Search Engine** | Meilisearch |
| 🔡 **OCR Processing** | Tesseract OCR |
| 📈 **Analytics** | Metabase |
| 🐳 **Containerization** | Docker · Docker Compose |
| 🌳 **Version Control** | Git & GitHub |

</div>

---

## 📂 Project Structure

```bash
naac-data-management-system/
│
├── frontend/              # React + Vite client
│   ├── src/
│   ├── public/
│   └── package.json
│
├── backend/                # Django REST API
│   ├── api/
│   ├── documents/
│   ├── reports/
│   ├── users/
│   └── manage.py
│
├── docker/                 # Docker configs
├── docs/                   # Documentation
├── uploads/                 # Local upload cache
├── docker-compose.yml
├── .env.example
└── README.md
```

---

## 🚀 Quick Start

> **Prerequisites:** Docker, Docker Compose, and Git installed and verified.
> ```bash
> docker --version
> docker-compose --version
> git --version
> ```

<details open>
<summary><strong>Step 1 — Clone the repository</strong></summary>

```bash
git clone <repository-url>
cd naac-data-management-system
```
</details>

<details open>
<summary><strong>Step 2 — Configure environment variables</strong></summary>

```bash
cp .env.example .env
```
Update the `.env` file with your required configuration values.
</details>

<details open>
<summary><strong>Step 3 — Start all services</strong></summary>

```bash
docker-compose up --build
```
</details>

<details open>
<summary><strong>Step 4 — Apply database migrations</strong></summary>

In a new terminal:
```bash
docker-compose exec backend python manage.py migrate
```
</details>

<details open>
<summary><strong>Step 5 — Create an admin user</strong></summary>

```bash
docker-compose exec backend python manage.py createsuperuser
```
</details>

<details open>
<summary><strong>Step 6 — Configure Keycloak</strong></summary>

1. Open **http://localhost:8080**
2. Sign in with the default credentials:
   ```text
   Username: admin
   Password: admin
   ```
3. Import the realm config: `keycloak-realm-config.json`
</details>

<details open>
<summary><strong>Step 7 — Configure Metabase</strong></summary>

1. Open **http://localhost:3000**
2. Connect Metabase to PostgreSQL
3. Build your analytics dashboards
</details>

---

## 🌐 Application URLs

| Service | URL |
|:---|:---|
| 🖥️ Frontend | http://localhost:3000 |
| ⚙️ Backend API | http://localhost:8000 |
| 🔐 Keycloak | http://localhost:8080 |
| 📦 MinIO Console | http://localhost:9001 |
| 🔎 Meilisearch | http://localhost:7700 |
| 📈 Metabase | http://localhost:3000 |

---

## 📚 API Endpoints

<details>
<summary><strong>🔐 Authentication</strong></summary>

```http
POST /api/auth/login/
```
</details>

<details>
<summary><strong>📁 Documents</strong></summary>

```http
GET  /api/documents/criteria/
POST /api/documents/upload/
GET  /api/documents/search/?q=<query>
```
</details>

<details>
<summary><strong>📄 Reports</strong></summary>

```http
GET /api/reports/naac/<criteria>/
```
</details>

---

## 💻 Local Development

<table>
<tr>
<td valign="top" width="50%">

**Backend Setup**
```bash
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

</td>
<td valign="top" width="50%">

**Frontend Setup**
```bash
cd frontend
npm install
npm run dev
```

</td>
</tr>
</table>

---

## 🔒 Security Features

✅ JWT Authentication&nbsp;&nbsp;|&nbsp;&nbsp;✅ Role-Based Access Control&nbsp;&nbsp;|&nbsp;&nbsp;✅ Secure Document Storage
✅ Audit Logging&nbsp;&nbsp;|&nbsp;&nbsp;✅ Access Tracking&nbsp;&nbsp;|&nbsp;&nbsp;✅ API Protection&nbsp;&nbsp;|&nbsp;&nbsp;✅ Cloud Storage Integration

---

## ☁️ Production Deployment

### Infrastructure Recommendations
- ☁️ AWS RDS for PostgreSQL
- 🪣 AWS S3 for Object Storage
- 🌐 NGINX Reverse Proxy
- 🔒 SSL/TLS Certificates
- 📊 Monitoring & Logging
- 💾 Automated Backups

### Deployment Checklist
- [ ] Configure production environment variables
- [ ] Enable HTTPS
- [ ] Set up database backups
- [ ] Configure monitoring
- [ ] Enable centralized logging
- [ ] Harden security settings

---

## 🎯 Future Enhancements

- 🤖 AI-powered accreditation recommendations
- 📈 Advanced analytics and forecasting
- 📱 Mobile application support
- 🏫 Multi-institution deployment
- ⚙️ Workflow automation
- 📧 Email and notification services
- ✅ Document approval workflows
- 🔮 Accreditation score prediction

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

```bash
# 1. Fork the repository

# 2. Create a feature branch
git checkout -b feature-name

# 3. Commit your changes
git commit -m "Add new feature"

# 4. Push to your branch
git push origin feature-name

# 5. Open a Pull Request
```

---

## 👨‍💻 Author

<div align="center">

**Sohan D Souza**

Full Stack Developer&nbsp;•&nbsp;AI/ML Enthusiast&nbsp;•&nbsp;Salesforce Developer

</div>

---

<div align="center">

## ⭐ Support

If you found this project useful, consider giving it a **⭐ on GitHub** — it helps increase visibility and supports future development.

</div>

<details>
<summary><strong>🏷️ GitHub Topics</strong></summary>

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
</details>
