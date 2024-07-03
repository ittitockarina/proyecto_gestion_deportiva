# En urls.py de tu aplicación
from django.urls import path
from . import views

urlpatterns = [
    path('sponsors/', views.SponsorListCreateAPIView.as_view(), name='sponsor-list-create'),
    path('sponsors/<int:pk>/', views.SponsorDetailAPIView.as_view(), name='sponsor-detail'),
]
