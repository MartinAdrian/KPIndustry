# Generated by Django 5.1.4 on 2025-02-02 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('KPITracker', '0015_alter_projects_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='reopened',
        ),
    ]
