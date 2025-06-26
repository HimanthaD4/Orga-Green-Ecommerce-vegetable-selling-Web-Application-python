#!/bin/bash
echo "----- Starting build process -----"

# Install system dependencies
apt-get update && apt-get install -y \
    libpq-dev \
    python3-dev \
    gcc \
    postgresql-client

# Install Python dependencies
python -m pip install --upgrade pip
pip install psycopg2-binary  # Explicitly install psycopg2
pip install -r requirements.txt

# Django setup
python manage.py collectstatic --noinput
python manage.py migrate

echo "----- Build completed successfully -----"