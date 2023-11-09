from django.db import models
from django.contrib.auth.models import User


class OtherUserData(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    institution = models.CharField(max_length=100)
    institutional_mail = models.EmailField()

    avatar = models.ImageField(upload_to='avatars', null=True, blank=True)