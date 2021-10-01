from .base import *

DEBUG = False

ADMINS = [
    (
        'Blessed S', 'blessedsibanda.me@gmail.com'
    )
]

ALLOWED_HOSTS = ['elearning.com', 'www.elearning.com']

SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'e_learning',
        'USER': 'e_learning',
        'PASSWORD': '1234pass',
        'PORT': '5432',
        'HOST': '127.0.0.1',
    }
}
