# En urls.py de tu aplicación
from django.urls import path
from . import views

urlpatterns = [
    path('entrenamientos/', views.EntrenamientoListCreateAPIView.as_view(), name='entrenamiento-list-create'),
    path('entrenamientos/<int:pk>/', views.EntrenamientoDetailUpdateDeleteAPIView.as_view(), name='entrenamiento-detail-update-delete'),
]
