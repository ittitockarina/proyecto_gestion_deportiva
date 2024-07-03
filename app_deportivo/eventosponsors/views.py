# En views.py
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import EventoSponsor
from .serializers import EventoSponsorSerializer

class EventoSponsorListCreateAPIView(generics.ListCreateAPIView):
    queryset = EventoSponsor.objects.all()
    serializer_class = EventoSponsorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class EventoSponsorDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EventoSponsor.objects.all()
    serializer_class = EventoSponsorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
