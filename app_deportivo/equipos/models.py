from django.db import models
from entrenadores.models import Entrenador
from deportes.models import Deporte
from federaciones.models import Federacion
from usuarios.models import Usuario

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    entrenador = models.ForeignKey(Entrenador, on_delete=models.CASCADE)
    deporte = models.ForeignKey(Deporte, on_delete=models.CASCADE)
    federacion = models.ForeignKey(Federacion, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
