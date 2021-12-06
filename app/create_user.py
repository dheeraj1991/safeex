import os

import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lunar_phase.settings")
django.setup()
from django.contrib.auth.models import User

if not User.objects.filter(username='dheeraj.prasanth@gmail.com').exists():
    User.objects.create_superuser('dheeraj.prasanth@gmail.com', 'dheeraj.prasanth@gmail.com', 'jango@10')
    print("Super User Added")
user, created = User.objects.get_or_create(username='vasilii@safeex.com', email='vasilii@safeex.com')
if created:
    user.set_password('testpass123')
    user.save()
    print("Basic User Created")

