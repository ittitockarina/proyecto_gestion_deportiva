from django.db import models

class Instalacion(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    direccion = models.TextField(blank=True, null=True)
    capacidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    encargado = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
