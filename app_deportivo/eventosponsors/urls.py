# En urls.py de tu aplicación
from django.urls import path
from . import views

urlpatterns = [
    path('eventosponsors/', views.EventoSponsorListCreateAPIView.as_view(), name='eventosponsor-list-create'),
    path('eventosponsors/<int:pk>/', views.EventoSponsorDetailAPIView.as_view(), name='eventosponsor-detail'),
]
