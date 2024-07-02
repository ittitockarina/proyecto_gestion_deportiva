from django.db import models

# Create your models here.
class Deporte(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)