import os
from django.conf.global_settings import CSRF_TRUSTED_ORIGINS, STATIC_ROOT
from django.middleware.csrf import CSRF_ALLOWED_CHARS
from .settings import BASE_DIR
from .settings import *

ALLOWED_HOSTS = [os.environ['ПолітехCinema_HOST']]
CSRF_TRUSTED_ORIGINS = ['https://'+os.environ['ПолітехCinema_HOST']]
DEBUG = False
SECRET_KEY = os.environ['Cinema_SECRET_KEY']

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    'whitenoise.middleware.WhiteNoiseMiddleware',
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

STORAGES = {
    'default': {
        'BACKEND': 'django.core.files.storage.FileSystemStorage',
    },
    'staticfiles': {
        'BACKEND': 'whitenoise.storage.CompressedStaticFilesStorage',
    },
}

CONNECTION = os.environ['AZURE_ПолітехCinema_DB']
CONNECTION_STR = {pair.split('=')[0]: pair.split('=')[1] for pair in CONNECTION.split(' ')}


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': CONNECTION_STR['DjangoCinema'],
        'HOST': CONNECTION_STR['host'],
        'USER' : CONNECTION_STR['root'],
        'PASSWORD' : CONNECTION_STR['vika.17122005'],
    }
}

STATIC_ROOT = BASE_DIR / 'staticfiles'