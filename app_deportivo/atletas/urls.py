# atletas/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.AtletaListView.as_view(), name='atleta_list'),
    path('<int:pk>/', views.AtletaDetailView.as_view(), name='atleta_detail'),
    path('create/', views.AtletaCreateView.as_view(), name='atleta_create'),
    path('<int:pk>/update/', views.AtletaUpdateView.as_view(), name='atleta_update'),
    path('<int:pk>/delete/', views.AtletaDeleteView.as_view(), name='atleta_delete'),
]
