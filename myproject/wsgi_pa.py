import os
import sys

# Add your project directory to the sys.path
project_home = '/home/unnikrishnanaaa803/myproject'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Set the settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'myproject.settings'

# Import Django's WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
from whitenoise import WhiteNoise
application = WhiteNoise(application, root=os.path.join(project_home, 'staticfiles'))