from django.db import models

# Create your models here:
class Patients(models.Model):
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    height = models.FloatField()
    weight = models.FloatField()
    bloodGlucose = models.FloatField()
    triglycerides = models.FloatField()