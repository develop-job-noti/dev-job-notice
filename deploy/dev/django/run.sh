#!/bin/bash

echo "[*] exec run.sh"

mkdir -p data
mkdir -p log

poetry run pip list

poetry run python3 manage.py collectstatic --noinput
poetry run python3 manage.py makemigrations --noinput
poetry run python3 manage.py migrate

exec poetry run gunicorn config.wsgi:application --config=deploy/dev/django/gunicorn.conf.py
