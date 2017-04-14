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

MIDDLEWARE += [
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

STATIC_ROOT = join(BASE_DIR, "static")
STATIC_URL = "/static/"
