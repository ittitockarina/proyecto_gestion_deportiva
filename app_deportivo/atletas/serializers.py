# En serializers.py
from rest_framework import serializers
from .models import Atleta
from deportes.serializers import DeporteSerializer
from entrenadores.serializers import EntrenadorSerializer
from federaciones.serializers import FederacionSerializer
from equipos.serializers import EquipoSerializer
from app_deportivo.serializers import UserSerializer

class AtletaSerializer(serializers.ModelSerializer):
    deporte = DeporteSerializer()
    entrenador = EntrenadorSerializer()
    federacion = FederacionSerializer()
    equipo = EquipoSerializer()
    usuario = UserSerializer()

    class Meta:
        model = Atleta
        fields = '__all__'
