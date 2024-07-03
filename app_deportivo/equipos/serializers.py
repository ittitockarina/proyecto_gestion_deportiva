# En serializers.py
from rest_framework import serializers
from .models import Equipo
from entrenadores.serializers import EntrenadorSerializer
from deportes.serializers import DeporteSerializer
from federaciones.serializers import FederacionSerializer
from usuarios.serializers import UsuarioSerializer

class EquipoSerializer(serializers.ModelSerializer):
    entrenador = EntrenadorSerializer()
    deporte = DeporteSerializer()
    federacion = FederacionSerializer()
    usuario = UsuarioSerializer()

    class Meta:
        model = Equipo
        fields = '__all__'
