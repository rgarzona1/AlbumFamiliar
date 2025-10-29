from django.db import models

# Create your models here.

class Fotos(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    fecha = models.DateField()
    imagen= models.ImageField