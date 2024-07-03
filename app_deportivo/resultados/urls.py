# En urls.py de tu aplicación
from django.urls import path
from . import views

urlpatterns = [
    path('resultados/', views.ResultadoListCreateAPIView.as_view(), name='resultado-list-create'),
    path('resultados/<int:pk>/', views.ResultadoDetailAPIView.as_view(), name='resultado-detail'),
]
