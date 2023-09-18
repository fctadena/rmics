# Generated by Django 4.1.7 on 2023-09-11 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MaintenanceLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wo_seq_num', models.CharField(max_length=255)),
                ('machine_failure_breakdown', models.CharField(max_length=255)),
                ('description_of_work', models.TextField()),
                ('work_type', models.CharField(choices=[('Repair', 'Repair'), ('Preventive Maintenance', 'Preventive Maintenance'), ('Fabrication', 'Fabrication'), ('General Jobs', 'General Jobs')], max_length=50)),
                ('root_cause', models.TextField()),
                ('job_start', models.DateTimeField()),
                ('job_end', models.DateTimeField()),
                ('time_consumed', models.DurationField()),
                ('affecting_production', models.DurationField()),
                ('affecting_time', models.DurationField()),
                ('equipment_name', models.CharField(max_length=255)),
                ('equipment_code', models.CharField(max_length=255)),
                ('section', models.CharField(max_length=255)),
                ('affecting_bagging', models.BooleanField()),
                ('machine_failure', models.BooleanField()),
                ('type_of_stop_time', models.CharField(choices=[('Planned', 'Planned'), ('Unplanned', 'Unplanned')], max_length=20)),
                ('work_center', models.CharField(choices=[('Mechanical', 'Mechanical'), ('Electrical', 'Electrical'), ('Instrumentation & Controls', 'Instrumentation & Controls'), ('Fabrication', 'Fabrication'), ('Lubrication', 'Lubrication')], max_length=50)),
                ('personnel_assigned', models.CharField(max_length=255)),
                ('parts_replaced', models.CharField(max_length=255)),
                ('quantity_of_parts', models.IntegerField()),
                ('status', models.CharField(choices=[('Waiting for Parts', 'Waiting for Parts'), ('On-going', 'On-going'), ('Completed', 'Completed'), ('Pending', 'Pending')], max_length=20)),
                ('remarks', models.TextField()),
                ('spare_details', models.TextField()),
                ('notification_num', models.CharField(max_length=255)),
            ],
        ),
    ]
