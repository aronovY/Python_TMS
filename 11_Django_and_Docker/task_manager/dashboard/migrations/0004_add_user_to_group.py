from django.contrib.auth.models import User, Group
from django.db import migrations


def add_user_to_group(apps, schema_editor):
    managers = Group.objects.get(id=1)
    develops = Group.objects.get(id=2)
    users = User.objects.all()
    for i in range(1, len(users)):
        user = User.objects.get(id=i)
        if user.is_staff == True:
            user.groups.add(managers)
        else:
            user.groups.add(develops)


class Migration(migrations.Migration):
    dependencies = [
        ('dashboard', '0003_add_users'),
    ]

    operations = [
        migrations.RunPython(add_user_to_group)
    ]