# Generated by Django 3.0.3 on 2020-03-06 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_add_projects_and_issue'),
    ]

    operations = [
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Issue')),
            ],
        ),
    ]
