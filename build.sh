#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Navigate to the project directory
cd space-django
# Install dependencies using Poetry (if you're using Poetry)
# poetry install

# Activate the virtual environment (if you're using a virtual environment)
# source venv/bin/activate

# Apply database migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Restart the server (if necessary)
# systemctl restart your_application_service

echo "Build completed successfully"
