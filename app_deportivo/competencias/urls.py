# competencias/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.competencia_list, name='competencia_list'),
    path('<int:pk>/', views.competencia_detail, name='competencia_detail'),
    path('new/', views.competencia_new, name='competencia_new'),
    path('<int:pk>/edit/', views.competencia_edit, name='competencia_edit'),
    path('<int:pk>/delete/', views.competencia_delete, name='competencia_delete'),
]
