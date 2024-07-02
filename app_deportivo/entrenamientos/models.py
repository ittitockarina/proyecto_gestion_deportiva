from django.db import models
from entrenadores.models import Entrenador
from atletas.models import Atleta

class Entrenamiento(models.Model):
    entrenador = models.ForeignKey(Entrenador, on_delete=models.CASCADE)
    atleta = models.ForeignKey(Atleta, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"Entrenamiento de {self.atleta.nombre} con {self.entrenador.nombre} ({self.fecha_inicio} - {self.fecha_fin})"
