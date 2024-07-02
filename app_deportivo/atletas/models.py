from django.db import models
from deportes.models import Deporte 
from entrenadores.models import Entrenador
from federaciones.models import Federacion
from equipos.models import Equipo
from usuarios.models import Usuario

class Atleta(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=10)
    deporte = models.ForeignKey(Deporte, on_delete=models.CASCADE)
    entrenador = models.ForeignKey(Entrenador, on_delete=models.CASCADE)
    federacion = models.ForeignKey(Federacion, on_delete=models.CASCADE)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    email = models.EmailField(blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    faltas = models.TextField(blank=True, null=True)  # tarjeta amarilla, roja
