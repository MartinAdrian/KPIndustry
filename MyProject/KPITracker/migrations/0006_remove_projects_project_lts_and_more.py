# Generated by Django 5.1.4 on 2025-01-12 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('KPITracker', '0005_userlist_on_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='project_lts',
        ),
        migrations.RemoveField(
            model_name='projects',
            name='project_testers',
        ),
    ]
