from django.db import models
from competencias.models import Competencia
from atletas.models import Atleta

class ParticipacionAtleta(models.Model):
    atleta = models.ForeignKey(Atleta, on_delete=models.CASCADE)
    competencia = models.ForeignKey(Competencia, on_delete=models.CASCADE)
    resultado = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.atleta} - {self.competencia}"
