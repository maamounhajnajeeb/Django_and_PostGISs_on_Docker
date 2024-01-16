#!/bin/sh

set -e

python manage.py migrate

gunicorn --env DJANGO_SETTINGS_MODULE=API.settings -c python:config.gunicorn_config API.wsgi
