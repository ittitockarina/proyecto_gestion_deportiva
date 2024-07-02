from django.db import models
from competencias.models import Competencia
from atletas.models import Atleta

class Inscripcion(models.Model):
    atleta = models.ForeignKey(Atleta, on_delete=models.CASCADE)
    competencia = models.ForeignKey(Competencia, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateField()
    estado = models.CharField(max_length=20)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Inscripción de {self.atleta.nombre} en {self.competencia.nombre}'
