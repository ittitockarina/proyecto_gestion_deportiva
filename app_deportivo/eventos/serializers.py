# En serializers.py
from rest_framework import serializers
from .models import Evento
from instalaciones.serializers import InstalacionSerializer
from federaciones.serializers import FederacionSerializer

class EventoSerializer(serializers.ModelSerializer):
    instalacion = InstalacionSerializer()
    federacion = FederacionSerializer()

    class Meta:
        model = Evento
        fields = '__all__'
