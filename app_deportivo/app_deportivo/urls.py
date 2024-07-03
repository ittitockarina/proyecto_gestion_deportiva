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
from django.urls import path, include
from .views import index  # Asegúrate de importar 'index' correctamente desde '.views'

urlpatterns = [
    path('', index, name='index'),  # Ruta principal que usa la vista 'index'
    path('admin/', admin.site.urls),
    
    # Añade aquí las URLs de tus aplicaciones
    path('auth/', include('autenticacion.urls')),  # Ajusta según la estructura de tus aplicaciones
    path('atletas/', include('atletas.urls')),  # Ajusta según la estructura de tus aplicaciones
    path('categorias/', include('categorias.urls')),  # Ajusta según la estructura de tus aplicaciones
    path('competencias/', include('competencias.urls')),  # Ajusta según la estructura de tus aplicaciones
    path('deportes/', include('deportes.urls')),  # Ajusta según la estructura de tus aplicaciones
]