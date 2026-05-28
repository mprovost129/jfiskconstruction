import os
from django.core.exceptions import ImproperlyConfigured
from .base import *

DEBUG = False

DEFAULT_ALLOWED_HOSTS = [
    'jfiskconstruction.com',
    '.jfiskconstruction.com',
]

env_allowed_hosts = [
    host.strip()
    for host in os.environ.get('ALLOWED_HOSTS', '').split(',')
    if host.strip()
]
ALLOWED_HOSTS = list(dict.fromkeys([*DEFAULT_ALLOWED_HOSTS, *env_allowed_hosts]))

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
        'BACKEND': 'whitenoise.storage.CompressedStaticFilesStorage',
    },
}

# Avoid hard failures if a manifest entry is missing; serve the original path instead.
WHITENOISE_MANIFEST_STRICT = False

# Persistent DB connections
CONN_MAX_AGE = 60

DEFAULT_CSRF_TRUSTED_ORIGINS = [
    'https://jfiskconstruction.com',
    'https://www.jfiskconstruction.com',
]

env_csrf_trusted_origins = [
    origin.strip()
    for origin in os.environ.get('CSRF_TRUSTED_ORIGINS', '').split(',')
    if origin.strip()
]
CSRF_TRUSTED_ORIGINS = list(
    dict.fromkeys([*DEFAULT_CSRF_TRUSTED_ORIGINS, *env_csrf_trusted_origins])
)

# Uses LocMemCache from base.py — sufficient for a low-traffic marketing site

# HTTPS / security
# Trust Render's (and most reverse proxies') forwarded-proto header so Django
# knows the original request was HTTPS and does not issue an infinite redirect.
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

