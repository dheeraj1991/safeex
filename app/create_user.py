import os

import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lunar_phase.settings")
django.setup()
from django.contrib.auth.models import User

if not User.objects.filter(username='dheeraj.prasanth@gmail.com').exists():
    User.objects.create_superuser('dheeraj.prasanth@gmail.com', 'dheeraj.prasanth@gmail.com', 'jango@10')
User.objects.get_or_create(username='vasilii@safeex.com', email='vasilii@safeex.com', password='password@123')
