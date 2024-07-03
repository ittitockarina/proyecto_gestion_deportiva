# En views.py
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Resultado
from .serializers import ResultadoSerializer

class ResultadoListCreateAPIView(generics.ListCreateAPIView):
    queryset = Resultado.objects.all()
    serializer_class = ResultadoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ResultadoDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Resultado.objects.all()
    serializer_class = ResultadoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
