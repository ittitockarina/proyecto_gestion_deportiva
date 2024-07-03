# En serializers.py
from rest_framework import serializers
from .models import Resultado
from competencias.serializers import CompetenciaSerializer
from atletas.serializers import AtletaSerializer

class ResultadoSerializer(serializers.ModelSerializer):
    competencia = CompetenciaSerializer()
    atleta = AtletaSerializer()

    class Meta:
        model = Resultado
        fields = '__all__'
