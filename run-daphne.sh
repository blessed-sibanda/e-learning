# make sure nginx is running

export DJANGO_SETTINGS_MODULE=config.settings.pro

daphne -u /tmp/daphne.sock config.asgi:application


