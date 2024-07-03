# En views.py
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Entrenamiento
from .serializers import EntrenamientoSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class EntrenamientoListCreateAPIView(generics.ListCreateAPIView):
    queryset = Entrenamiento.objects.all()
    serializer_class = EntrenamientoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class EntrenamientoDetailUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Entrenamiento.objects.all()
    serializer_class = EntrenamientoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
