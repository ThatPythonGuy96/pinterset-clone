#! /usr/bin/env bash

set -o errexit   #  exit on error

pip install -r requirements.txt

python manage.py collectstatic --no-input

python manage.py makemigrations user
python manage.py makemigrations post
python manage.py migrate --no-input

echo "=== Creating initial data ==="
python manage.py shell << END
from user.models import User
import os

user, _ = User.objects.get_or_create(
    email='admin@gmail.com',
    username='admin',
    is_superuser=True,
    is_staff=True,
    is_active=True,
    is_admin=True
)
user.set_password('admin123')
user.save()

print("Initial data setup completed")
END

echo "=== Build completed successfully! ==="
