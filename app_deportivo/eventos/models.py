from django.db import models
from instalaciones.models import Instalacion
from federaciones.models import Federacion

class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()
    descripcion = models.TextField(blank=True, null=True)
    instalacion = models.ForeignKey(Instalacion, on_delete=models.CASCADE)
    federacion = models.ForeignKey(Federacion, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
