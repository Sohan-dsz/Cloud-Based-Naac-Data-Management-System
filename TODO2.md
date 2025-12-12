Current Work:
The NAAC Data Management System project has been partially implemented with Django backend, React frontend, and Docker services (Keycloak, MinIO, Meilisearch, Metabase). However, the user believes the codes are incomplete and wants to rewrite all code from the beginning, deleting unnecessary files, while ensuring all URLs are correct and the system is fully functional.

Key Technical Concepts:

Backend: Django REST Framework with custom authentication (Keycloak OIDC), document management (MinIO storage, Meilisearch indexing), reports (PDF generation), audit logging.
Frontend: React with Vite, Keycloak integration, components for login, upload, dashboard, search, analytics, reports.
Services: Docker Compose with PostgreSQL databases, Keycloak for auth, MinIO for storage, Meilisearch for search, Metabase for analytics.
URLs: Frontend http://localhost:5174, Backend http://localhost:8000, Keycloak http://localhost:8080, MinIO http://localhost:9001, Meilisearch http://localhost:7700, Metabase http://localhost:3001.
Relevant Files and Code:

All current files in backend/, frontend/, docker-compose.yml, keycloak-realm-config.json, etc., will be reviewed and rewritten from scratch to ensure completeness and correctness.
Unnecessary files will be deleted to start fresh.
Problem Solving:

Previous issues included redirect URI mismatches (fixed by updating to port 5174), but user wants a complete rewrite to avoid any incompleteness.
Ensure all integrations work: auth flow, document upload/search, analytics embed, report generation, audit logs.
Pending Tasks and Next Steps:

Delete unnecessary code files (e.g., any redundant or incomplete files).
Rewrite backend code: settings.py, models.py, views.py, serializers.py, urls.py for all apps (authentication, documents, reports, audit).
Rewrite frontend code: App.jsx, components (Login, UploadForm, EvidenceDashboard, Analytics, ReportDownload), vite.config.js, package.json.
Update configurations: docker-compose.yml, keycloak-realm-config.json to ensure correct URLs and ports.
Test the system: Run docker-compose, verify frontend/backend access, test auth flow, document operations, search, analytics, reports.
Confirm all URLs are working without mismatches.