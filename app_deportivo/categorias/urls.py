# categorias/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.categoria_list, name='categoria_list'),
    path('<int:pk>/', views.categoria_detail, name='categoria_detail'),
    path('new/', views.categoria_new, name='categoria_new'),
    path('<int:pk>/edit/', views.categoria_edit, name='categoria_edit'),
    path('<int:pk>/delete/', views.categoria_delete, name='categoria_delete'),
]
