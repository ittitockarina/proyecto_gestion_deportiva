# En views.py
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import ParticipacionAtleta
from .serializers import ParticipacionAtletaSerializer

class ParticipacionAtletaListCreateAPIView(generics.ListCreateAPIView):
    queryset = ParticipacionAtleta.objects.all()
    serializer_class = ParticipacionAtletaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ParticipacionAtletaDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ParticipacionAtleta.objects.all()
    serializer_class = ParticipacionAtletaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
