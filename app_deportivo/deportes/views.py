from django.shortcuts import get_object_or_404, redirect
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Deporte
from .serializers import DeporteSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class DeporteListCreateAPIView(generics.ListCreateAPIView):
    queryset = Deporte.objects.all()
    serializer_class = DeporteSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class DeporteDetailUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Deporte.objects.all()
    serializer_class = DeporteSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
