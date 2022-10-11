from django.db import models

# Create your models here.


class Familiar(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField()
    edad = models.IntegerField()
    email = models.EmailField()

