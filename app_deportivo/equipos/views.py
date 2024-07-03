# En views.py
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Equipo
from .serializers import EquipoSerializer

class EquipoListCreateAPIView(generics.ListCreateAPIView):
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class EquipoDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
