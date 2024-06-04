from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Deporte, Entrenador, Federacion, Equipo, Atleta, Instalacion, Disciplina, Categoria, Competencia, Medalla, Resultado, Inscripcion, Usuario, Evento, Sponsor, EventoSponsor, ParticipacionAtleta, Entrenamiento


def index(request):
    return render(request, 'index.html')
# List Views
class DeporteListView(ListView):
    model = Deporte
    template_name = 'deporte_list.html'
    context_object_name = 'deportes'

class EntrenadorListView(ListView):
    model = Entrenador
    template_name = 'entrenador_list.html'
    context_object_name = 'entrenadores'

# Detail Views
class DeporteDetailView(DetailView):
    model = Deporte
    template_name = 'deporte_detail.html'
    context_object_name = 'deporte'

class EntrenadorDetailView(DetailView):
    model = Entrenador
    template_name = 'entrenador_detail.html'
    context_object_name = 'entrenador'

# Create Views
class DeporteCreateView(CreateView):
    model = Deporte
    template_name = 'deporte_form.html'
    fields = ['nombre', 'descripcion']
    success_url = reverse_lazy('deporte_list')

class EntrenadorCreateView(CreateView):
    model = Entrenador
    template_name = 'entrenador_form.html'
    fields = ['nombre', 'apellido', 'especialidad', 'email', 'telefono']
    success_url = reverse_lazy('entrenador_list')

# Update Views
class DeporteUpdateView(UpdateView):
    model = Deporte
    template_name = 'deporte_form.html'
    fields = ['nombre', 'descripcion']
    success_url = reverse_lazy('deporte_list')

class EntrenadorUpdateView(UpdateView):
    model = Entrenador
    template_name = 'entrenador_form.html'
    fields = ['nombre', 'apellido', 'especialidad', 'email', 'telefono']
    success_url = reverse_lazy('entrenador_list')

# Delete Views
class DeporteDeleteView(DeleteView):
    model = Deporte
    template_name = 'deporte_confirm_delete.html'
    success_url = reverse_lazy('deporte_list')

class EntrenadorDeleteView(DeleteView):
    model = Entrenador
    template_name = 'entrenador_confirm_delete.html'
    success_url = reverse_lazy('entrenador_list')
