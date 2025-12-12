# NAAC Data Management System Rewrite Plan

## 1. Clean Up Project
- [ ] Delete unnecessary files (TODO.md, TODO2.md, .env.example if not needed)
- [ ] Keep only essential structure: docker-compose.yml, keycloak-realm-config.json, backend/ (empty structure), frontend/ (empty structure)

## 2. Rewrite Backend (Django)
- [ ] Update backend/naac_system/settings.py with correct configurations (databases, auth, CORS for 5174, services URLs)
- [ ] Rewrite backend/apps/authentication/models.py (User, Role models)
- [ ] Rewrite backend/apps/authentication/auth.py (KeycloakAuthentication)
- [ ] Rewrite backend/apps/authentication/views.py (login, logout, profile views)
- [ ] Rewrite backend/apps/authentication/serializers.py (UserSerializer, etc.)
- [ ] Rewrite backend/apps/authentication/urls.py (auth endpoints)
- [ ] Rewrite backend/apps/documents/models.py (Criteria, Evidence, Document models)
- [ ] Rewrite backend/apps/documents/views.py (upload, search, list views)
- [ ] Rewrite backend/apps/documents/serializers.py (DocumentSerializer, etc.)
- [ ] Rewrite backend/apps/documents/urls.py (document endpoints)
- [ ] Rewrite backend/apps/reports/views.py (PDF report generation)
- [ ] Rewrite backend/apps/reports/urls.py (report endpoints)
- [ ] Rewrite backend/apps/audit/models.py (AuditLog model)
- [ ] Rewrite backend/apps/audit/middleware.py (AuditMiddleware)
- [ ] Rewrite backend/apps/audit/views.py (AuditLogListView)
- [ ] Rewrite backend/apps/audit/serializers.py (AuditLogSerializer)
- [ ] Rewrite backend/apps/audit/urls.py (audit endpoints)
- [ ] Update backend/naac_system/urls.py (include all app URLs)
- [ ] Update backend/requirements.txt (ensure all dependencies)

## 3. Rewrite Frontend (React + Vite)
- [ ] Update frontend/package.json (dependencies: react, axios, @react-keycloak/web, etc.)
- [ ] Update frontend/vite.config.js (proxy to localhost:8000)
- [ ] Rewrite frontend/src/App.jsx (routing, Keycloak provider, auth guards)
- [ ] Rewrite frontend/src/components/Login.jsx (Keycloak login integration)
- [ ] Rewrite frontend/src/components/UploadForm.jsx (file upload with criteria selection)
- [ ] Rewrite frontend/src/components/EvidenceDashboard.jsx (document list, search, approve)
- [ ] Rewrite frontend/src/components/Analytics.jsx (Metabase iframe embed)
- [ ] Rewrite frontend/src/components/ReportDownload.jsx (criteria selection, PDF download)
- [ ] Update frontend/src/index.css (Tailwind styles)
- [ ] Update frontend/src/main.jsx (React app entry)

## 4. Update Configurations
- [ ] Update docker-compose.yml (correct ports: frontend 5174, backend 8000, etc., CORS origins)
- [ ] Update keycloak-realm-config.json (redirect URIs and web origins to 5174)

## 5. Test and Verify
- [ ] Run docker-compose up --build -d
- [ ] Verify all services start correctly
- [ ] Test frontend access at http://localhost:5174
- [ ] Test backend API at http://localhost:8000
- [ ] Test Keycloak auth flow (login, redirect)
- [ ] Test document upload and search
- [ ] Test analytics embed
- [ ] Test report generation
- [ ] Confirm all URLs work without mismatches
