from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dni = models.CharField(max_length=9, unique=True, null=True, blank=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=9, null=True, blank=True)
    rol = models.CharField(
        max_length=50, 
        choices=[
            ('atleta', 'Atleta'), 
            ('entrenador', 'Entrenador'), 
            ('administrador', 'Administrador')
        ]
    )

    def __str__(self):
        return self.user.username
