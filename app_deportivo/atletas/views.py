from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Atleta

# List View
class AtletaListView(ListView):
    model = Atleta
    template_name = 'deportes/atleta_list.html'  # Asegúrate de crear esta plantilla
    context_object_name = 'atletas'

class AtletaDetailView(DetailView):
    model = Atleta
    template_name = 'deportes/atleta_detail.html'  # Asegúrate de crear esta plantilla
    context_object_name = 'atleta'

class AtletaCreateView(CreateView):
    model = Atleta
    template_name = 'deportes/atleta_form.html'  # Asegúrate de crear esta plantilla
    fields = ['nombre', 'apellido', 'fecha_nacimiento', 'genero', 'deporte', 'entrenador', 'federacion', 'equipo', 'email', 'telefono', 'usuario', 'faltas']
    success_url = reverse_lazy('atleta_list')

class AtletaUpdateView(UpdateView):
    model = Atleta
    template_name = 'deportes/atleta_form.html'  # Asegúrate de crear esta plantilla
    fields = ['nombre', 'apellido', 'fecha_nacimiento', 'genero', 'deporte', 'entrenador', 'federacion', 'equipo', 'email', 'telefono', 'usuario', 'faltas']
    success_url = reverse_lazy('atleta_list')

class AtletaDeleteView(DeleteView):
    model = Atleta
    template_name = 'deportes/atleta_confirm_delete.html'  # Asegúrate de crear esta plantilla
    success_url = reverse_lazy('atleta_list')
