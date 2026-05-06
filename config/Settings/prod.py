import os
from django.core.exceptions import ImproperlyConfigured
from .base import *

DEBUG = False

ALLOWED_HOSTS = os.environ['ALLOWED_HOSTS'].split(',')

# Fail fast if no database is configured
if not os.environ.get('DATABASE_URL') and not os.environ.get('DB_HOST'):
    raise ImproperlyConfigured(
        'Production requires either DATABASE_URL or DB_HOST to be set.'
    )

# Whitenoise — insert after SecurityMiddleware
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')

STORAGES = {
    'default': {
        'BACKEND': 'django.core.files.storage.FileSystemStorage',
    },
    'staticfiles': {
        'BACKEND': 'whitenoise.storage.CompressedManifestStaticFilesStorage',
    },
}

# Avoid hard failures if a manifest entry is missing; serve the original path instead.
WHITENOISE_MANIFEST_STRICT = False

# Persistent DB connections
CONN_MAX_AGE = 60

CSRF_TRUSTED_ORIGINS = os.environ.get('CSRF_TRUSTED_ORIGINS', '').split(',')

# Uses LocMemCache from base.py — sufficient for a low-traffic marketing site

# HTTPS / security
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

