# Generated by Django 5.1.4 on 2025-01-12 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KPITracker', '0003_rename_projectlts_projects_project_lts_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Ongoing'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='project_lts',
            field=models.JSONField(null=True, verbose_name='Project LTs'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='project_testers',
            field=models.JSONField(null=True, verbose_name='Project Testers'),
        ),
    ]
