# En views.py
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Entrenador
from .serializers import EntrenadorSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class EntrenadorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Entrenador.objects.all()
    serializer_class = EntrenadorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class EntrenadorDetailUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Entrenador.objects.all()
    serializer_class = EntrenadorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
