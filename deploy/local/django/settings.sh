#!/bin/bash

echo "[*] setting django service"

mkdir log
mkdir data


python3 manage.py collectstatic --noinput
python3 manage.py makemigrations --noinput
python3 manage.py migrate

# gunicorn config.wsgi:application --config=deploy/gunicorn.conf.py
