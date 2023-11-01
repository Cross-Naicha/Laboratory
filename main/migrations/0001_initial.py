# Generated by Django 4.2.6 on 2023-10-31 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('height', models.FloatField()),
                ('weight', models.FloatField()),
                ('bloodGlucose', models.FloatField()),
                ('triglycerides', models.FloatField()),
            ],
        ),
    ]