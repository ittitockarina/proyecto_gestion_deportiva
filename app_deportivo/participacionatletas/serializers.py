# En serializers.py
from rest_framework import serializers
from .models import ParticipacionAtleta
from competencias.serializers import CompetenciaSerializer
from atletas.serializers import AtletaSerializer

class ParticipacionAtletaSerializer(serializers.ModelSerializer):
    atleta = AtletaSerializer()
    competencia = CompetenciaSerializer()

    class Meta:
        model = ParticipacionAtleta
        fields = '__all__'
