from .base import * 

DEBUG = True

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

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