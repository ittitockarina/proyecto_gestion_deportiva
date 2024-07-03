# En serializers.py
from rest_framework import serializers
from .models import Medalla
from competencias.serializers import CompetenciaSerializer

class MedallaSerializer(serializers.ModelSerializer):
    competencia = CompetenciaSerializer()

    class Meta:
        model = Medalla
        fields = '__all__'
