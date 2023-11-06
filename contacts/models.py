from django.db import models

class Suscriptors(models.Model):    
    email = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.email}'
