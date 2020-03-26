from django.contrib.auth.models import Permission, Group
from django.db import migrations
from dashboard import apps


def add_permissions(apps, schema_editor):
    all_permission = Permission.objects.all()
    permission_to_dev = Permission.objects.filter(name__in=['Can view issue', 'Can view project'])
    manager_group = Group.objects.get(name='Manager')
    developer_group = Group.objects.get(name='Developer')

    manager_group.permissions.add(*all_permission)
    developer_group.permissions.add(*permission_to_dev)


class Migration(migrations.Migration):
    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('dashboard', '0004_add_user_to_group'),
    ]

    operations = [
        migrations.RunPython(add_permissions)
    ]


# from django.contrib.auth.models import Group
# from django.db import migrations
# from django.contrib.auth.management import create_permissions
# from django.apps import apps
#
# APPS = []
#
#
# def create_applications_permissions():
#     for app in APPS:
#         app_config = apps.get_app_config(app)
#         create_permissions(app_config)
#
#
# def add_permissions(apps, schema_editor):
#     create_applications_permissions()
#     Permission = apps.get_model('auth', 'Permission')
#     manager_group = Group.objects.get(name='Manager')
#     developer_group = Group.objects.get(name='Developer')
#     can_add = Permission.objects.all()
#     permission_to_dev = Permission.objects.filter(name__in=['Can view issue', 'Can view project'])
#     manager_group.permissions.add(*can_add)
#     developer_group.permissions.add(*permission_to_dev)
#     manager_group.save()
#     developer_group.save()
#
#
# class Migration(migrations.Migration):
#     dependencies = [
#         ('auth', '0011_update_proxy_permissions'),
#         ('dashboard', '0004_add_user_to_group'),
#     ]
#
#     operations = [
#         migrations.RunPython(add_permissions)
#     ]