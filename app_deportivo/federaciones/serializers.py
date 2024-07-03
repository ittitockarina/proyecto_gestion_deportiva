# En serializers.py
from rest_framework import serializers
from .models import Federacion

class FederacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Federacion
        fields = '__all__'
