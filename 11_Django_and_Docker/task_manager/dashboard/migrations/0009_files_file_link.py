# Generated by Django 3.0.3 on 2020-03-20 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_project_users_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='files',
            name='file_link',
            field=models.FileField(blank=True, null=True, upload_to='logos'),
        ),
    ]