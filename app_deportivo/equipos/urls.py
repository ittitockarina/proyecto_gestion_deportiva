# En urls.py de tu aplicación
from django.urls import path
from . import views

urlpatterns = [
    path('equipos/', views.EquipoListCreateAPIView.as_view(), name='equipo-list-create'),
    path('equipos/<int:pk>/', views.EquipoDetailAPIView.as_view(), name='equipo-detail'),
]
