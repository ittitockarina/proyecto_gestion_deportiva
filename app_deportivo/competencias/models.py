from django.db import models
from deportes.models import Deporte
from instalaciones.models import Instalacion
from disciplinas.models import Disciplina
from categorias.models import Categoria

class Competencia(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    deporte = models.ForeignKey(Deporte, on_delete=models.CASCADE)
    instalacion = models.ForeignKey(Instalacion, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    def __str__(self):
            return self.nombre