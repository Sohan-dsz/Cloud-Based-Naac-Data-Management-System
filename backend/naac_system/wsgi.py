"""
WSGI config for NAAC Data Management System project.
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'naac_system.settings')

application = get_wsgi_application()