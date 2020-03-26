from dashboard import models
from django.utils import timezone
from django.db import migrations
import csv


def add_projects(apps, schema_editor):
    path = '/Users/user/Desktop/Python/12_lesson/task_manager/dashboard/migrations/data/projects.csv'
    with open(path) as file:
        reader = csv.DictReader(file, delimiter=',')
        for line in reader:
            models.Project.objects.create(
                name=line['name'],
                description=line['description'],
                created_at=timezone.now()
            )


def add_issues(apps, schema_editor):
    path = '/Users/user/Desktop/Python/12_lesson/task_manager/dashboard/migrations/data/issues.csv'
    with open(path) as file:
        reader = csv.DictReader(file, delimiter=',')
        for line in reader:
            models.Issue.objects.create(
                created_at=timezone.now(),
                name=line['name'],
                description=line['description'],
                deadline=line['deadline'],
                assigne_id=line['assigne_id'],
                project_id=line['project_id'],
                reported_id=line['reported_id']
            )


class Migration(migrations.Migration):
    dependencies = [
        ('dashboard', '0005_add_permission'),
    ]

    operations = [
        migrations.RunPython(add_projects),
        migrations.RunPython(add_issues)
    ]