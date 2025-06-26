#!/bin/bash
echo "----- Starting build process -----"

# Update and install system dependencies
apt-get update && apt-get install -y \
    libpq-dev \
    python3-dev \
    gcc \
    postgresql-client

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate

# Upgrade pip and install Python dependencies from E_shop/requirements.txt
python -m pip install --upgrade pip
pip install -r E_shop/requirements.txt

# Change directory to Django project
cd E_shop

# Collect static files without user input
python manage.py collectstatic --noinput

# Apply database migrations
python manage.py migrate

echo "----- Build completed successfully -----"
