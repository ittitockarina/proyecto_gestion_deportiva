# En urls.py de tu aplicación
from django.urls import path
from . import views

urlpatterns = [
    path('federaciones/', views.FederacionListCreateAPIView.as_view(), name='federacion-list-create'),
    path('federaciones/<int:pk>/', views.FederacionDetailAPIView.as_view(), name='federacion-detail'),
]
