#!/usr/bin/env bash 

root=$1
source $root/venv/bin/activate 

export DJANGO_SETTINGS_MODULE=config.settings.pro 

cd $root/django/

python manage.py collectstatic
