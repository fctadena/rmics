# Generated by Django 4.1.7 on 2023-09-18 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drms', '0002_maintenancelog_include_log_maintenancelog_system_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintenancelog',
            name='affecting_production',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='maintenancelog',
            name='affecting_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='maintenancelog',
            name='time_consumed',
            field=models.TimeField(),
        ),
    ]