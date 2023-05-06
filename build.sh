#!/usr/bin/env bash
# exit on error
set -o errexit

poetry install
cd batelecom
python manage.py collectstatic --no-input
python manage.py migrate
