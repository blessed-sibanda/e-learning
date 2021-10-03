from .base import *
import os

DEBUG = False

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

ADMINS = [
    (
        'Blessed S', 'blessedsibanda.me@gmail.com'
    )
]

ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS').split(',')


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
