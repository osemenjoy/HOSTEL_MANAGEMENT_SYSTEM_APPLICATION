import os
import sys
import django

# Ensure project root is on sys.path so we can import settings when running from scripts/
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hostel_project.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

matric = 'admin123'
pw = 'pass1234'

if not User.objects.filter(matric_number=matric).exists():
    User.objects.create_superuser(matric_number=matric, password=pw, first_name='Admin')
    print('Created default superuser:', matric)
else:
    print('Superuser already exists')
