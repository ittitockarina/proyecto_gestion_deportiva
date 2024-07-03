# En urls.py de tu aplicación
from django.urls import path
from . import views

urlpatterns = [
    path('inscripciones/', views.InscripcionListCreateAPIView.as_view(), name='inscripcion-list-create'),
    path('inscripciones/<int:pk>/', views.InscripcionDetailAPIView.as_view(), name='inscripcion-detail'),
]
