#!/bin/bash
python manage.py collectstatic --noinput

sudo systemctl restart nginx

pkill gunicorn || true

gunicorn Teste.wsgi:application --bind 127.0.0.1:8000 &