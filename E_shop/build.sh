#!/bin/bash
echo "----- Starting build process -----"

# Install system dependencies
apt-get update && apt-get install -y \
    libpq-dev \
    python3-dev \
    gcc \
    postgresql-client

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate

# Install Python dependencies with explicit psycopg2 installation
python -m pip install --upgrade pip
pip install psycopg2-binary==2.9.7 --no-cache-dir
pip install -r requirements.txt

# Django setup
python manage.py collectstatic --noinput
python manage.py migrate

echo "----- Build completed successfully -----"