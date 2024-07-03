# En views.py
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Atleta
from .serializers import AtletaSerializer

class AtletaListCreateAPIView(generics.ListCreateAPIView):
    queryset = Atleta.objects.all()
    serializer_class = AtletaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class AtletaDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Atleta.objects.all()
    serializer_class = AtletaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
