# Generated by Django 5.0.4 on 2024-05-20 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MAINTENANCE', '0002_remove_maintenancerequest_check_repaired_by_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintenancerequest',
            name='date_of_request',
            field=models.DateField(auto_now_add=True),
        ),
    ]
