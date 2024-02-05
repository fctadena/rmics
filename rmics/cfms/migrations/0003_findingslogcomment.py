# Generated by Django 4.1.7 on 2024-02-05 14:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cfms', '0002_findingslog_log_reporter'),
    ]

    operations = [
        migrations.CreateModel(
            name='FindingsLogComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.TextField(max_length=1000)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('commenter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('findings_log', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='findings_log_comments', to='cfms.findingslog')),
            ],
            options={
                'ordering': ('timestamp',),
            },
        ),
    ]