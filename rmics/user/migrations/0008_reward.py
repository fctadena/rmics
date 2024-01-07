# Generated by Django 4.1.7 on 2023-12-25 14:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0007_alter_customuserprofile_profile_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('certificate', models.FileField(blank=True, null=True, upload_to='certificates/', verbose_name='certificate')),
                ('awardee', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='awardee')),
            ],
        ),
    ]