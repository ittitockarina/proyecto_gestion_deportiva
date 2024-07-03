# En urls.py de tu aplicación
from django.urls import path
from . import views

urlpatterns = [
    path('participaciones/', views.ParticipacionAtletaListCreateAPIView.as_view(), name='participacion-list-create'),
    path('participaciones/<int:pk>/', views.ParticipacionAtletaDetailAPIView.as_view(), name='participacion-detail'),
]
