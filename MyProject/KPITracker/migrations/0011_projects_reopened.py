# Generated by Django 5.1.4 on 2025-01-14 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KPITracker', '0010_projects_end_date_projects_start_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='reopened',
            field=models.BooleanField(default=False),
        ),
    ]
