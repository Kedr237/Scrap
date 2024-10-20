#!/bin/sh

until nc -z $POSTGRES_HOST $POSTGRES_PORT; do
    sleep 1
done

cd src

python manage.py migrate

python manage.py test

gunicorn settings.wsgi:application --bind 0.0.0.0:8000