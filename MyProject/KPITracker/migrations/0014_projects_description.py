# Generated by Django 5.1.4 on 2025-01-24 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KPITracker', '0013_alter_userlist_on_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='description',
            field=models.CharField(blank=True, max_length=2000, null=True, verbose_name='Project Description'),
        ),
    ]
