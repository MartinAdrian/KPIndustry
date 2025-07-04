# Generated by Django 5.1.4 on 2025-02-12 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KPITracker', '0027_delete_locationsregistered'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocationsRegistered',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Location Name')),
                ('lat', models.CharField(max_length=200, verbose_name='Latitude')),
                ('lon', models.CharField(max_length=200, verbose_name='Longitude')),
                ('country', models.CharField(max_length=200, verbose_name='Country')),
                ('region', models.CharField(max_length=200, verbose_name='Region')),
                ('city', models.CharField(max_length=200, verbose_name='City')),
                ('street', models.CharField(max_length=200, verbose_name='Street')),
                ('number', models.CharField(max_length=200, verbose_name='Number')),
                ('zipcode', models.IntegerField(verbose_name='Zip Code')),
                ('misc_description', models.CharField(max_length=800, null=True, verbose_name='Misc Description')),
            ],
        ),
    ]
