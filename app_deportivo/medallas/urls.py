# En urls.py de tu aplicación
from django.urls import path
from . import views

urlpatterns = [
    path('medallas/', views.MedallaListCreateAPIView.as_view(), name='medalla-list-create'),
    path('medallas/<int:pk>/', views.MedallaDetailAPIView.as_view(), name='medalla-detail'),
]
