# En serializers.py
from rest_framework import serializers
from .models import Inscripcion
from competencias.serializers import CompetenciaSerializer
from atletas.serializers import AtletaSerializer

class InscripcionSerializer(serializers.ModelSerializer):
    competencia = CompetenciaSerializer()
    atleta = AtletaSerializer()

    class Meta:
        model = Inscripcion
        fields = '__all__'
