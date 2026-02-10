#!/usr/bin/env bash
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Change directory into the Django project folder
cd grocerymate

# Collect static files
python manage.py collectstatic --no-input

# Run migrations
python manage.py migrate
