# TODO List Feature Implementation Plan

## Backend (Django/DRF)
- [x] Create tasks app structure: `backend/apps/tasks/` with `__init__.py`, `apps.py`, `models.py`, `views.py`, `serializers.py`, `urls.py`, `migrations/`
- [x] Define Task model in `models.py` (title, description, status, due_date, priority, assigned_to, created_by, related_criteria, timestamps)
- [ ] Create TaskSerializer in `serializers.py` (ModelSerializer with nested UserSerializer, validation)
- [ ] Implement views in `views.py` (TaskListCreateView, TaskRetrieveUpdateDestroyView, TaskMyView with permissions)
- [ ] Define URLs in `urls.py` (`/api/tasks/`, `/api/tasks/<id>/`, `/api/tasks/my/`)
- [ ] Update `backend/naac_system/settings.py`: Add `'apps.tasks'` to INSTALLED_APPS
- [ ] Update `backend/naac_system/urls.py`: Include tasks URLs
- [ ] Run migrations: `python manage.py makemigrations tasks && python manage.py migrate`

## Frontend (React)
- [ ] Create TaskList.jsx component (fetch/display tasks, filter by user)
- [ ] Create TaskForm.jsx component (create/edit form with criteria dropdown, due_date, assign user)
- [ ] Update App.jsx: Add routes for tasks (`/tasks`, `/tasks/new`, `/tasks/<id>`) with auth guards

## Testing and Verification
- [ ] Test backend API endpoints with Postman/curl (create, list, update as different roles)
- [ ] Test frontend UI: Login, view/create tasks, confirm auth and permissions
- [ ] Verify integration: Audit logs, no CORS errors, links to Criteria
- [ ] Full system test: Run `docker-compose up --build`, access tasks at http://localhost:5174/tasks
