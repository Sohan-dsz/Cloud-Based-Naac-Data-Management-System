# NAAC Data Management System - Error Fixes Plan

## Backend Fixes
- [ ] Implement missing models in backend/apps/authentication/models.py (if any, but User and Role seem present)
- [ ] Implement missing models in backend/apps/documents/models.py (Criteria, Evidence, Document)
- [ ] Implement missing models in backend/apps/reports/models.py (if any)
- [ ] Implement missing models in backend/apps/tasks/models.py (Task)
- [ ] Add missing views in backend/apps/authentication/views.py (LogoutView, ProfileView)
- [ ] Add missing views in backend/apps/documents/views.py (DocumentUploadView, DocumentListView, DocumentSearchView)
- [ ] Add missing views in backend/apps/reports/views.py (ReportGenerateView)
- [ ] Add missing views in backend/apps/tasks/views.py (TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView)
- [ ] Add missing serializers in backend/apps/authentication/serializers.py (LoginSerializer, KeycloakTokenSerializer, RoleSerializer)
- [ ] Add missing serializers in backend/apps/documents/serializers.py (CriteriaSerializer, EvidenceSerializer, DocumentSerializer)
- [ ] Add missing serializers in backend/apps/tasks/serializers.py (TaskSerializer)
- [ ] Add missing URL patterns in backend/apps/authentication/urls.py (login, logout, profile, roles)
- [ ] Add missing URL patterns in backend/apps/documents/urls.py (upload, list, search)
- [ ] Add missing URL patterns in backend/apps/reports/urls.py (generate)
- [ ] Add missing URL patterns in backend/apps/tasks/urls.py (list, create, update, delete)
- [ ] Update backend/naac_system/urls.py to include all app URLs

## Frontend Fixes
- [ ] Add 'import React from "react";' to frontend/src/App.jsx
- [ ] Add 'import React from "react";' to frontend/src/components/Login.jsx
- [ ] Add 'import React from "react";' to frontend/src/components/UploadForm.jsx
- [ ] Add 'import React from "react";' to frontend/src/components/EvidenceDashboard.jsx
- [ ] Add 'import React from "react";' to frontend/src/components/ReportDownload.jsx
- [ ] Add 'import React from "react";' to frontend/src/components/Analytics.jsx

## Configuration Fixes
- [ ] Update docker-compose.yml (correct ports: frontend 5174, backend 8000, etc., CORS origins)
- [ ] Update keycloak-realm-config.json (redirect URIs and web origins to 5174)
- [ ] Update backend/naac_system/settings.py (databases, auth, CORS for 5174, services URLs)
- [ ] Update frontend/vite.config.js (proxy to localhost:8000)

## Testing
- [ ] Run docker-compose up --build -d
- [ ] Verify all services start correctly
- [ ] Test frontend access at http://localhost:5174
- [ ] Test backend API at http://localhost:8000
- [ ] Test Keycloak auth flow (login, redirect)
- [ ] Test document upload and search
- [ ] Test analytics embed
- [ ] Test report generation
- [ ] Confirm all URLs work without mismatches
