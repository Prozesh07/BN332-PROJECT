# Generated by Django 5.1 on 2024-09-28 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0006_alter_appointment_patient'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='patient',
        ),
        migrations.AddField(
            model_name='appointment',
            name='patient_contact_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='patient_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='patient_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
