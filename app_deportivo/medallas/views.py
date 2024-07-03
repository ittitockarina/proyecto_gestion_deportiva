# En views.py
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Medalla
from .serializers import MedallaSerializer

class MedallaListCreateAPIView(generics.ListCreateAPIView):
    queryset = Medalla.objects.all()
    serializer_class = MedallaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class MedallaDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Medalla.objects.all()
    serializer_class = MedallaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
