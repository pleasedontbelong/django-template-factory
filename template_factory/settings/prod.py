# https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

from .base import *  # NOQA
from os import environ
from os.path import join


DEBUG = False
TEMPLATE_DEBUG = False
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

SECRET_KEY = environ['SECRET_KEY']

PARENT_HOST = 'django-template-factory.herokuapp.com'
ALLOWED_HOSTS = ['.%s' % PARENT_HOST]
SESSION_COOKIE_DOMAIN = ALLOWED_HOSTS[0]
SESSION_COOKIE_NAME = 'django-template-factory'
CSRF_COOKIE_DOMAIN = PARENT_HOST
CSRF_TRUSTED_ORIGINS = [PARENT_HOST]

MIDDLEWARE += [
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

STATIC_ROOT = join(BASE_DIR, "static")
STATIC_URL = "/static/"

FORCE_SSL = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        },
    },
}

GENERATOR_DRY_RUN = False
