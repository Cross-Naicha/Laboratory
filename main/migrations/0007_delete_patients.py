# Generated by Django 4.2.6 on 2023-11-07 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_delete_doctors'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Patients',
        ),
    ]
