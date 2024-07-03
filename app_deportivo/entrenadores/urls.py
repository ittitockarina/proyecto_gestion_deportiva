# En urls.py de tu aplicación
from django.urls import path
from . import views

urlpatterns = [
    path('entrenadores/', views.EntrenadorListCreateAPIView.as_view(), name='entrenador-list-create'),
    path('entrenadores/<int:pk>/', views.EntrenadorDetailUpdateDeleteAPIView.as_view(), name='entrenador-detail-update-delete'),
]
