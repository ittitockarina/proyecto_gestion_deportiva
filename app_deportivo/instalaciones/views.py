# En views.py
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Instalacion
from .serializers import InstalacionSerializer

class InstalacionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Instalacion.objects.all()
    serializer_class = InstalacionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class InstalacionDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Instalacion.objects.all()
    serializer_class = InstalacionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
