#!/usr/bin/env sh

cd /opt/app
[ ! -d "./docker/venv" ] && python -m venv ./docker/venv
source docker/venv/bin/activate
pip install -r requirements/production.txt
source development_envvars.sh
# Overwrite some envvars for docker usage
export DJANGO_DB_HOST="postgres"
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
