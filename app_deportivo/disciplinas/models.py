from django.db import models
from deportes.models import Deporte

class Disciplina(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    deporte = models.ForeignKey(Deporte, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
