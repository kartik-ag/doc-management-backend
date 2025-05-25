"""
WSGI config for doc_management project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'doc_management.settings')

application = get_wsgi_application() 