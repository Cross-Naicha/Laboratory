from django.db import models

# Create your models here:
class Patients(models.Model):
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    height = models.FloatField()
    weight = models.FloatField()
    bloodGlucose = models.FloatField()
    triglycerides = models.FloatField()

    def __str__(self):
        return f'{self.id} - {self.lastname}, {self.name}'
    
class Doctors(models.Model):
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    field = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.id} - {self.lastname}, {self.name}. {self.field}'
    
class Suscriptors(models.Model):    
    email = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.email}'