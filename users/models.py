from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

AGE_CHOICES = [tuple([x,x]) for x in range(15,91)]

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True,blank=True,choices = AGE_CHOICES)
