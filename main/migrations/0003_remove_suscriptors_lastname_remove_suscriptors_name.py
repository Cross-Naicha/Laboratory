# Generated by Django 4.2.6 on 2023-11-01 23:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_doctors_suscriptors'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='suscriptors',
            name='lastname',
        ),
        migrations.RemoveField(
            model_name='suscriptors',
            name='name',
        ),
    ]
