#!/bin/sh

until nc -z $POSTGRES_HOST $POSTGRES_PORT; do
    sleep 1
done

gunicorn -w 2 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000 src.main:app