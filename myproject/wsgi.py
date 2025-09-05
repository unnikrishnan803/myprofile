"""
WSGI config for myproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

application = get_wsgi_application()

# Vercel handler function
def handler(event, context):
    from django.core.handlers.wsgi import WSGIHandler
    from django.conf import settings
    import sys
    from io import StringIO

    # Set up Django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

    # Create WSGI handler
    django_handler = WSGIHandler()

    # Convert Vercel event to WSGI environ
    environ = {
        'REQUEST_METHOD': event.get('httpMethod', 'GET'),
        'SCRIPT_NAME': '',
        'PATH_INFO': event.get('path', '/'),
        'QUERY_STRING': event.get('queryStringParameters', {}) or '',
        'CONTENT_TYPE': event.get('headers', {}).get('content-type', ''),
        'CONTENT_LENGTH': str(len(event.get('body', ''))),
        'SERVER_NAME': 'vercel',
        'SERVER_PORT': '443',
        'wsgi.version': (1, 0),
        'wsgi.url_scheme': 'https',
        'wsgi.input': StringIO(event.get('body', '')),
        'wsgi.errors': sys.stderr,
        'wsgi.multithread': False,
        'wsgi.multiprocess': False,
        'wsgi.run_once': False,
    }

    # Add headers
    for key, value in event.get('headers', {}).items():
        environ[f'HTTP_{key.upper().replace("-", "_")}'] = value

    # Handle the request
    response = django_handler(environ, lambda status, headers: start_response(status, headers))

    return {
        'statusCode': int(status.split()[0]),
        'headers': dict(headers),
        'body': ''.join(response)
    }

def start_response(status, headers):
    global response_status, response_headers
    response_status = status
    response_headers = headers

# Also export app for compatibility
app = application
