import os
from django.conf.global_settings import CSRF_TRUSTED_ORIGINS, STATIC_ROOT
from django.middleware.csrf import CSRF_ALLOWED_CHARS
from .settings import BASE_DIR
from .settings import *

ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']]
CSRF_TRUSTED_ORIGINS = ['https://'+os.environ['WEBSITE_HOSTNAME']]
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

CONNECTION = os.environ['AZURE_MYSQL_CONNECTIONSTRING']
CONNECTION_STR = {pair.split('=')[0]: pair.split('=')[1] for pair in CONNECTION.split(' ')}


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'djangocinema-database',
        'USER' : 'psvgmnughg',
        'PASSWORD' : '$HXyhzE4xnfcPX25',
        'HOST': 'djangocinema-server.mysql.database.azure.com',
    }
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': CONNECTION_STR['Database'],
#         'HOST': CONNECTION_STR['Server'],
#         'USER' : CONNECTION_STR['User Id'],
#         'PASSWORD' : CONNECTION_STR['Password'],
#     }
# }

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')