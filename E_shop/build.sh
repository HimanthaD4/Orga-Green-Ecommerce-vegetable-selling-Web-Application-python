#!/bin/bash

# Always run from repo root
cd "$(dirname "$0")"  # ensures inside E_shop

python -m venv venv
source venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt

python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate
