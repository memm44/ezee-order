from decouple import config

from .base import *

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Puedes usar SQLite para el entorno de desarrollo
DATABASES['default'] = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': BASE_DIR / 'db.sqlite3',
}

# Usamos emails en consola durante el desarrollo para no enviar correos reales
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config('DEV_EMAIL_HOST')
EMAIL_HOST_USER = config('DEV_EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('DEV_EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = config('DEV_DEFAULT_FROM_EMAIL')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
# No es necesario tener el nivel de seguridad más alto en desarrollo
