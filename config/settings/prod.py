from .base import *

DEBUG = False

ALLOWED_HOSTS = ['www.tudominio.com']

# Base de datos de producción
DATABASES['default'] = {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'production_db',
    'USER': 'production_user',
    'PASSWORD': config('PRODUCTION_DB_PASSWORD'),
    'HOST': 'localhost',
    'PORT': '5432',
}

# Usamos un servidor de correos real para producción
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config('PRD_EMAIL_HOST')
EMAIL_HOST_USER = config('PRD_EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('PRD_EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = config('PRD_DEFAULT_FROM_EMAIL')
EMAIL_PORT = config('PRD_EMAIL_PORT')
EMAIL_USE_TLS = config('PRD_EMAIL_USE_TLS')