# Generated by Django 5.0.4 on 2024-05-20 15:01

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MAINTENANCE', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='maintenancerequest',
            name='check_repaired_by',
        ),
        migrations.AddField(
            model_name='maintenancerequest',
            name='check_repaired_by',
            field=models.ManyToManyField(related_name='checked_requests', to=settings.AUTH_USER_MODEL),
        ),
    ]
