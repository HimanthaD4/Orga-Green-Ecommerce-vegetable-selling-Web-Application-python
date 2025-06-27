#!/bin/bash
echo "----- Starting build process -----"

apt-get update && apt-get install -y \
    libpq-dev \
    python3-dev \
    gcc \
    postgresql-client

python -m venv venv
source venv/bin/activate

python -m pip install --upgrade pip

# You are already in the E_shop directory when running build.sh
pip install -r requirements.txt

# Collect static files from correct location
python manage.py collectstatic --noinput

# Apply migrations
python manage.py migrate

echo "----- Build completed successfully -----"
