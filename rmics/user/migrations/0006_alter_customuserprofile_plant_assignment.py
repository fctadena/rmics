# Generated by Django 4.1.7 on 2023-12-07 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ams', '0007_plantassignment'),
        ('user', '0005_delete_plantassignment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuserprofile',
            name='plant_assignment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ams.plantassignment'),
        ),
    ]