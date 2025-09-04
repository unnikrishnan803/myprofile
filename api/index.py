import os
import sys
import django
from django.core.wsgi import get_wsgi_application

# Add the project directory to the Python path
project_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, project_dir)

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# Initialize Django
django.setup()

# Get the WSGI application
application = get_wsgi_application()

def handler(request, **kwargs):
    return application