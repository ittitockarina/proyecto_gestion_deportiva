"""
URL configuration for app_deportivo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import path
from .views import (index,DeporteListView, DeporteDetailView, DeporteCreateView, DeporteUpdateView, DeporteDeleteView,
                    EntrenadorListView, EntrenadorDetailView, EntrenadorCreateView, EntrenadorUpdateView, EntrenadorDeleteView)

urlpatterns = [
    path('', index, name='index'),
    path("admin/", admin.site.urls),
    # Aquí van tus otras rutas
    # Deporte URLs
    path('deportes/', DeporteListView.as_view(), name='deporte_list'),
    path('deportes/<int:pk>/', DeporteDetailView.as_view(), name='deporte_detail'),
    path('deportes/new/', DeporteCreateView.as_view(), name='deporte_new'),
    path('deportes/<int:pk>/edit/', DeporteUpdateView.as_view(), name='deporte_edit'),
    path('deportes/<int:pk>/delete/', DeporteDeleteView.as_view(), name='deporte_delete'),

    # Entrenador URLs
    path('entrenadores/', EntrenadorListView.as_view(), name='entrenador_list'),
    path('entrenadores/<int:pk>/', EntrenadorDetailView.as_view(), name='entrenador_detail'),
    path('entrenadores/new/', EntrenadorCreateView.as_view(), name='entrenador_new'),
    path('entrenadores/<int:pk>/edit/', EntrenadorUpdateView.as_view(), name='entrenador_edit'),
    path('entrenadores/<int:pk>/delete/', EntrenadorDeleteView.as_view(), name='entrenador_delete'),
]
