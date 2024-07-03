# En urls.py de tu aplicación
from django.urls import path
from . import views

urlpatterns = [
    path('disciplinas/', views.DisciplinaListCreateAPIView.as_view(), name='disciplina-list-create'),
    path('disciplinas/<int:pk>/', views.DisciplinaDetailUpdateDeleteAPIView.as_view(), name='disciplina-detail-update-delete'),
]
