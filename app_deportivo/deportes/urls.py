# deportes/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.deporte_list, name='deporte_list'),
    path('<int:pk>/', views.deporte_detail, name='deporte_detail'),
    path('new/', views.deporte_new, name='deporte_new'),
    path('<int:pk>/edit/', views.deporte_edit, name='deporte_edit'),
    path('<int:pk>/delete/', views.deporte_delete, name='deporte_delete'),
]
