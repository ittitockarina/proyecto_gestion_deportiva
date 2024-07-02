from django.db import models
from competencias.models import Competencia
from atletas.models import Atleta

class Resultado(models.Model):
    competencia = models.ForeignKey(Competencia, on_delete=models.CASCADE)
    atleta = models.ForeignKey(Atleta, on_delete=models.CASCADE)
    posicion = models.IntegerField()
    tiempo = models.TimeField()
    puntos = models.IntegerField()

    def __str__(self):
        return f"{self.competencia} - {self.atleta} - Posición: {self.posicion}"
