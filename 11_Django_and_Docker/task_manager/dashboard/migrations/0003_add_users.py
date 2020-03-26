from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.hashers import make_password
from django.db import migrations
import csv


def add_users(apps, schema_editor):
    path = '/Users/user/Desktop/Python/12_lesson/task_manager/dashboard/migrations/data/team.csv'
    with open(path) as file:
        reader = csv.DictReader(file, delimiter=',')
        for line in reader:
            User.objects.create(
                password=make_password(line['password']),
                last_login=timezone.now(),
                is_superuser=bool(line['is_superuser']),
                username=line['username'],
                first_name=line['first_name'],
                last_name=line['last_name'],
                email=line['email'],
                is_staff=bool(line['is_staff']))


class Migration(migrations.Migration):
    dependencies = [
        ('dashboard', '0002_create_group'),
    ]

    operations = [
        migrations.RunPython(add_users)
    ]