# Generated by Django 5.1.2 on 2025-02-02 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_appointment_doctor_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='available_days',
            new_name='available_day',
        ),
    ]
