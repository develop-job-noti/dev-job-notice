#!/bin/bash

echo "[*] exec run.sh"

mkdir -p data

# Start Xvfb (virtual framebuffer)
Xvfb :99 -screen 0 1024x768x16 &

# Export display environment variable
export DISPLAY=:99

python3 manage.py collectstatic --noinput
python3 manage.py makemigrations --noinput
python3 manage.py migrate

exec gunicorn config.wsgi:application --config=deploy/dev/django/gunicorn.conf.py
