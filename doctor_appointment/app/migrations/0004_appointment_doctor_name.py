# Generated by Django 5.1.2 on 2025-02-01 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='doctor_name',
            field=models.CharField(default='Dr. Unknown', max_length=255),
        ),
    ]
