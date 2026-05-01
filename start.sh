#!/usr/bin/env bash
set -e

echo "Instalando dependências..."
pip install -r requirements.txt

echo "Coletando arquivos estáticos..."
python manage.py collectstatic --noinput

echo "Iniciando aplicação..."
gunicorn Teste.wsgi:application --bind 0.0.0.0:$PORT