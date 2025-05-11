from .base import *

DEBUG = False

ALLOWED_HOSTS = ['STG.tudominio.com']

# Puedes usar PostgreSQL o la base de datos real de pre-producción
DATABASES['default'] = {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'STG_db',
    'USER': 'STG_user',
    'PASSWORD': config('STG_DB_PASSWORD'),
    'HOST': 'localhost',
    'PORT': '5432',
}

# Usamos un servidor de correos real para STG
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config('STG_EMAIL_HOST')
EMAIL_HOST_USER = config('STG_EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('STG_EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = config('STG_DEFAULT_FROM_EMAIL')
EMAIL_PORT = config('STG_EMAIL_PORT')
EMAIL_USE_TLS = config('STG_EMAIL_USE_TLS')