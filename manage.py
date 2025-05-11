#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

from decouple import config
from django.core.management import execute_from_command_line


os.environ.setdefault('DJANGO_SETTINGS_MODULE', config('DJANGO_SETTINGS_MODULE'))

if os.getenv('DJANGO_ENV') == 'staging':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.staging')
elif os.getenv('DJANGO_ENV') == 'production':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.production')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.dev')

execute_from_command_line(sys.argv)