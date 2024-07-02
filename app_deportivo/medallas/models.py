from django.db import models
from competencias.models import Competencia

class Medalla(models.Model):
    tipo = models.CharField(max_length=10)
    descripcion = models.CharField(max_length=20)
    competencia = models.ForeignKey(Competencia, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.tipo} - {self.competencia}"
