# En serializers.py
from rest_framework import serializers
from .models import EventoSponsor
from eventos.serializers import EventoSerializer
from sponsors.serializers import SponsorSerializer

class EventoSponsorSerializer(serializers.ModelSerializer):
    evento = EventoSerializer()
    sponsor = SponsorSerializer()

    class Meta:
        model = EventoSponsor
        fields = '__all__'
