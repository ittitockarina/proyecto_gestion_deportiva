from django.db import models
from eventos.models import Evento
from sponsors.models import Sponsor

class EventoSponsor(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.evento.nombre} - {self.sponsor.nombre}"
