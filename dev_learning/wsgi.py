"""
WSGI config for dev_learning project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
import sys

# Add your project directory to the sys.path
sys.path.append('/home/pathhive21/dev_learning')

# Set the Django settings module for your project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dev_learning.settings')

# Import the WSGI application and make it available as `application`
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

