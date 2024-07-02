# categorias/models.py
from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    edad_minima = models.IntegerField()
    edad_maxima = models.IntegerField()

    def __str__(self):
        return self.nombre
