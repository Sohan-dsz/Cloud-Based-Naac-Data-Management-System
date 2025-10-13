# 🌐 Cloud-Based NAAC Data Management and Accreditation Support System

A centralized, secure, and cloud-ready platform to **store, manage, and analyze institutional data** for NAAC accreditation.  
Built entirely with your own code and Dockerized for easy setup.

---

## 🚀 Features

- 🔒 **Role-based Authentication** – via Keycloak (`iqac_admin`, `dept_admin`, `faculty`, `student`)
- 📂 **Document Management** – upload and version control for NAAC evidence
- 🔍 **Search & OCR** – Meilisearch-powered fast search with OCR capabilities
- 📊 **Analytics** – Metabase dashboards for NAAC criteria analysis
- 🧾 **Report Generation** – automatic PDF reports for accreditation
- 🧠 **Audit Logging** – comprehensive tracking of all user actions
- 🌐 **Cloud-Ready** – fully containerized with Docker Compose
- 📱 **Responsive UI** – Bootstrap-based responsive frontend

---

## 🧱 Tech Stack

| Layer | Technology |
|--------|-------------|
| **Frontend** | React + TypeScript + Vite + Bootstrap |
| **Backend** | Django + Django REST Framework |
| **Database** | PostgreSQL |
| **Object Storage** | MinIO (S3 compatible) |
| **Authentication** | Keycloak (OIDC / JWT) |
| **Search** | Meilisearch with OCR |
| **Analytics** | Metabase |
| **Containerization** | Docker + Docker Compose |
| **Reverse Proxy** | Nginx |

---

## ⚙️ Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop)  
- [Docker Compose](https://docs.docker.com/compose/install/)  
- Optional: [VS Code](https://code.visualstudio.com/) for editing

No manual Python / Node setup required — everything runs inside containers.

---

## 🚀 Quick Start

### 1. Clone and Navigate
```bash
git clone <repository-url>
cd naac-data-management-system
```

### 2. Start All Services
```bash
docker-compose up -d
```

### 3. Access the Application
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/swagger/
- **Keycloak Admin**: http://localhost:8080 (admin/admin_password)
- **MinIO Console**: http://localhost:9001 (minio_admin/minio_password)
- **Meilisearch**: http://localhost:7700
- **Metabase**: http://localhost:3001

### 4. Initialize the Database
```bash
docker-compose exec backend python manage.py migrate
docker-compose exec backend python manage.py createsuperuser
```

---

## 📂 Project Structure

```
naac-data-management-system/
├── backend/                    # Django Backend
│   ├── apps/                  # Django Applications
│   │   ├── authentication/   # User management & Keycloak integration
│   │   ├── documents/         # Document management & storage
│   │   ├── analytics/         # Analytics and reporting
│   │   └── audit/            # Audit logging
│   ├── naac_system/          # Django project settings
│   ├── requirements.txt      # Python dependencies
│   └── Dockerfile           # Backend container config
├── frontend/                  # React Frontend
│   ├── src/
│   │   ├── components/       # Reusable components
│   │   ├── pages/            # Page components
│   │   ├── services/         # API services
│   │   ├── hooks/            # Custom React hooks
│   │   └── utils/           # Utility functions
│   ├── package.json         # Node dependencies
│   └── Dockerfile          # Frontend container config
├── config/                   # Configuration files
│   ├── nginx.conf           # Nginx configuration
│   └── init-db.sql         # Database initialization
├── docs/                     # Documentation
├── scripts/                  # Utility scripts
├── docker-compose.yml       # Container orchestration
├── .env                     # Environment variables
└── README.md               # This file
```

---

## 🔧 Development Setup

### Backend Development
```bash
cd backend
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows
pip install -r requirements.txt
python manage.py runserver
```

### Frontend Development
```bash
cd frontend
npm install
npm run dev
```

### Running Individual Services
```bash
# Start only database and supporting services
docker-compose up -d postgres minio keycloak meilisearch

# Run backend locally
cd backend
python manage.py runserver

# Run frontend locally
cd frontend
npm run dev
```

---

## 🏗️ Architecture Overview

### Authentication Flow
1. User authenticates via Keycloak
2. JWT tokens are issued and validated
3. Role-based access control enforced

### Document Management Flow
1. Documents uploaded via React frontend
2. Files stored in MinIO object storage
3. Metadata stored in PostgreSQL
4. OCR processing for searchable text
5. Full-text search via Meilisearch

### Analytics Flow
1. Data aggregated in PostgreSQL
2. Metabase connects for visualization
3. Custom dashboards for NAAC criteria
4. Automated report generation

---

## 🔐 Security Features

- **HTTPS/TLS** encryption in production
- **JWT-based** authentication with Keycloak
- **Role-based access control** (RBAC)
- **Audit logging** for all operations
- **Secure file upload** validation
- **CORS** protection
- **Environment variable** configuration

---

## 📊 NAAC Criteria Support

The system supports all NAAC criteria categories:

1. **Curricular Aspects**
2. **Teaching-Learning and Evaluation**
3. **Research, Innovations and Extension**
4. **Infrastructure and Learning Resources**
5. **Student Support and Progression**
6. **Governance, Leadership and Management**
7. **Institutional Values and Best Practices**

---

## 🚢 Deployment

### Production Deployment
1. Update environment variables in `.env`
2. Configure domain and SSL certificates
3. Run: `docker-compose -f docker-compose.prod.yml up -d`

### Cloud Deployment
- **AWS**: Use ECS/EKS with RDS and S3
- **Google Cloud**: Use GKE with Cloud SQL and Cloud Storage
- **Azure**: Use AKS with Azure Database and Blob Storage

---

## 🧪 Testing

```bash
# Backend tests
docker-compose exec backend python manage.py test

# Frontend tests
docker-compose exec frontend npm test

# End-to-end tests
docker-compose exec frontend npm run e2e
```

---

## 📚 API Documentation

Access the interactive API documentation at:
- **Swagger UI**: http://localhost:8000/swagger/
- **ReDoc**: http://localhost:8000/redoc/

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🆘 Support & Troubleshooting

### Common Issues

**Issue**: Services not starting
```bash
docker-compose down
docker-compose up -d --build
```

**Issue**: Database connection errors
```bash
docker-compose exec postgres psql -U naac_user -d naac_db
```

**Issue**: Frontend build errors
```bash
docker-compose exec frontend npm install
docker-compose exec frontend npm run build
```

### Getting Help

- Check the [Issues](https://github.com/your-repo/issues) page
- Contact: support@naac-system.com
- Documentation: [Wiki](https://github.com/your-repo/wiki)

---

## 🗺️ Roadmap

- [ ] Mobile application
- [ ] Advanced analytics with AI/ML
- [ ] Integration with external systems
- [ ] Multi-tenant support
- [ ] Advanced workflow automation
- [ ] Integration with plagiarism detection tools

---

**Made with ❤️ for educational institutions pursuing NAAC accreditation**