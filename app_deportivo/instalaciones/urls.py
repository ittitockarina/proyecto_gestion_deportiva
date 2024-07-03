# En urls.py de tu aplicación
from django.urls import path
from . import views

urlpatterns = [
    path('instalaciones/', views.InstalacionListCreateAPIView.as_view(), name='instalacion-list-create'),
    path('instalaciones/<int:pk>/', views.InstalacionDetailAPIView.as_view(), name='instalacion-detail'),
]
