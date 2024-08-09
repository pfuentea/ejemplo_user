from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Usuario(AbstractUser):
    rut = models.CharField(max_length=20)

class Propiedad(models.Model):
    nombre= models.CharField(max_length=50)