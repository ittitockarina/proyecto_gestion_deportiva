from django.db import models

class Sponsor(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    contacto = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre
