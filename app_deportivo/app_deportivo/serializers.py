# En serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Usuario

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class UsuarioSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Usuario
        fields = '__all__'
