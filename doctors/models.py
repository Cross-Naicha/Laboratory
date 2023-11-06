from django.db import models


class Doctors(models.Model):
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    field = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.id} - {self.lastname}, {self.name}. {self.field}'
