from .base import *
import os

DEBUG = False

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

assert SECRET_KEY is not None, \
    'Please provide DJANGO_SECRET_KET environment variable with a value'

ADMINS = [
    (
        'Blessed S', 'blessedsibanda.me@gmail.com'
    )
]

ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS')

SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DJANGO_DB_NAME'),
        'USER': os.getenv('DJANGO_DB_USER'),
        'PASSWORD': os.getenv('DJANGO_DB_PASSWORD'),
        'HOST': os.getenv('DJANGO_DB_HOST'),
        'PORT': os.getenv('DJANGO_DB_PORT'),
    }
}
