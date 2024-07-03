# En views.py
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Federacion
from .serializers import FederacionSerializer

class FederacionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Federacion.objects.all()
    serializer_class = FederacionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class FederacionDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Federacion.objects.all()
    serializer_class = FederacionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
