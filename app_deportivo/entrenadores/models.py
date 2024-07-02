from django.db import models
from deportes.models import Deporte
from usuarios.models import Usuario

# Create your models here.
class Entrenador(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    especialidad = models.ForeignKey(Deporte, on_delete=models.CASCADE)
    email = models.EmailField(blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"