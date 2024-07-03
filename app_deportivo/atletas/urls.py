# atletas/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('atletas/', views.AtletaListCreateAPIView.as_view(), name='atleta-list-create'),
    path('atletas/<int:pk>/', views.AtletaDetailAPIView.as_view(), name='atleta-detail'),
]
