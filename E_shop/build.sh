#!/bin/bash
echo "----- Starting build process -----"

# Install system dependencies
apt-get update && apt-get install -y \
    libpq-dev \
    python3-dev \
    gcc

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate

# Install Python dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Django setup
python manage.py collectstatic --noinput
python manage.py migrate

echo "----- Build completed successfully -----"