from rest_framework import serializers
from django.contrib.auth.models import User
from app_deportivo.models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'password', 'dni', 'nombre', 'apellido', 'telefono', 'rol']

    def create(self, validated_data):
        # Extraer datos del usuario
        username = validated_data.pop('username')
        email = validated_data.pop('email')
        password = validated_data.pop('password')

        # Crear el usuario de Django
        user = User.objects.create_user(username=username, email=email, password=password)

        # Crear el usuario de la aplicación
        usuario = Usuario.objects.create(user=user, **validated_data)
        return usuario