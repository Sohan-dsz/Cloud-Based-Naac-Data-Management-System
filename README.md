# Cloud-Based NAAC Data Management and Accreditation Support System

A centralized, secure, and scalable platform to store, manage, and analyze institutional data for NAAC accreditation.

## Features

- **Authentication & Roles**: Keycloak-based authentication with role-based access (iqac_admin, dept_admin, faculty, student)
- **Document Management**: Upload, version control, and organization of NAAC-related documents
- **Search & Retrieval**: Meilisearch-powered fast document search with OCR text extraction
- **Dashboards & Analytics**: Metabase-embedded analytics dashboards
- **Report Generation**: Automated PDF reports for NAAC criteria
- **Audit Logging**: Comprehensive logging of all user actions

## Tech Stack

- **Frontend**: React.js + Vite + Bootstrap
- **Backend**: Django + Django REST Framework
- **Database**: PostgreSQL
- **Object Storage**: MinIO (S3-compatible)
- **Authentication**: Keycloak (OIDC/JWT)
- **Search Engine**: Meilisearch
- **Analytics**: Metabase
- **Containerization**: Docker + Docker Compose

## Prerequisites

- Docker and Docker Compose
- Git

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd naac-data-management-system
   ```

2. **Environment Configuration**:
   ```bash
   cp .env.example .env
   # Edit .env with your specific configurations
   ```

3. **Build and Start Services**:
   ```bash
   docker-compose up --build
   ```

4. **Database Migrations** (in a separate terminal):
   ```bash
   docker-compose exec backend python manage.py migrate
   ```

5. **Create Superuser** (optional):
   ```bash
   docker-compose exec backend python manage.py createsuperuser
   ```

6. **Configure Keycloak**:
   - Access Keycloak at http://localhost:8080
   - Login with admin/admin
   - Import the realm from `keycloak-realm-config.json`

7. **Configure Metabase**:
   - Access Metabase at http://localhost:3000
   - Connect to PostgreSQL database
   - Create dashboards for NAAC analytics

## Usage

1. **Access the Application**:
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - MinIO Console: http://localhost:9001 (minioadmin/minioadmin)
   - Meilisearch: http://localhost:7700

2. **Login**: Use Keycloak authentication

3. **Upload Documents**: Navigate to upload page, select NAAC criteria and evidence

4. **Search Documents**: Use the dashboard search functionality

5. **View Analytics**: Access embedded Metabase dashboards

6. **Generate Reports**: Download PDF reports for specific NAAC criteria

## API Endpoints

- `POST /api/auth/login/` - User login
- `GET /api/documents/criteria/` - List NAAC criteria
- `POST /api/documents/upload/` - Upload document
- `GET /api/documents/search/?q=<query>` - Search documents
- `GET /api/reports/naac/<criteria>/` - Generate NAAC report

## Development

### Backend
```bash
cd backend
pip install -r requirements.txt
python manage.py runserver
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

## Deployment

This system is designed to be cloud-ready. For production deployment:

1. Update environment variables for production settings
2. Use managed services (RDS for PostgreSQL, S3 for MinIO, etc.)
3. Configure proper SSL/TLS
4. Set up monitoring and logging
5. Implement backup strategies

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License.
