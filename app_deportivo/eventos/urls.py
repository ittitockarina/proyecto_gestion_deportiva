# En urls.py de tu aplicación
from django.urls import path
from . import views

urlpatterns = [
    path('eventos/', views.EventoListCreateAPIView.as_view(), name='evento-list-create'),
    path('eventos/<int:pk>/', views.EventoDetailAPIView.as_view(), name='evento-detail'),
]
