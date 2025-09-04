import os
import sys
import django
from django.core.wsgi import get_wsgi_application
from django.core.management import execute_from_command_line
from django.conf import settings

# Add the project directory to the Python path
project_dir = os.path.dirname(__file__)
sys.path.insert(0, project_dir)

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# Configure Django for Vercel
settings.configure(
    DEBUG=False,
    SECRET_KEY=os.environ.get('SECRET_KEY', 'vercel-secret-key'),
    ALLOWED_HOSTS=['*'],
    INSTALLED_APPS=[
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'myapp',
    ],
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:',
        }
    },
    STATIC_URL='/static/',
    STATIC_ROOT='/tmp/staticfiles',
    MEDIA_URL='/media/',
    MEDIA_ROOT='/tmp/media',
    ROOT_URLCONF='myproject.urls',
    MIDDLEWARE=[
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ],
    TEMPLATES=[
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ],
)

# Initialize Django
django.setup()

# Run migrations for in-memory database
from django.core.management import call_command
call_command('migrate', verbosity=0, interactive=False)

# Get the WSGI application
application = get_wsgi_application()

def handler(request, **kwargs):
    return application