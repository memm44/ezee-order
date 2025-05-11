"""
WSGI config for servixia_site project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'servixia_site.settings')
#
# application = get_wsgi_application()
import os

from django.core.wsgi import get_wsgi_application

if os.getenv('DJANGO_ENV') == 'staging':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.staging')
elif os.getenv('DJANGO_ENV') == 'production':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.production')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.dev')

application = get_wsgi_application()