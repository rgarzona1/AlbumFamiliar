from django.db import models

# Create your models here.

class Fotos(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    fecha = models.DateField()
    imagen = models.ImageField(upload_to='fotos/', null=True, blank=True)