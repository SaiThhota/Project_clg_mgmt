#!/usr/bin/env bash

python manage.py migrate
python manage.py collectstatic --noinput
gunicorn TASK1.Clg_administration.wsgi:application