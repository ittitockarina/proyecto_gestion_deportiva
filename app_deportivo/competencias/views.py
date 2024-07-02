# competencias/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Competencia


def competencia_list(request):
    competencias = Competencia.objects.all()
    return render(request, 'competencias/competencia_list.html', {'competencias': competencias})
# competencias/views.py
def competencia_detail(request, pk):
    competencia = get_object_or_404(Competencia, pk=pk)
    return render(request, 'competencias/competencia_detail.html', {'competencia': competencia})
# competencias/views.py
def competencia_new(request):
    if request.method == "POST":
        form = CompetenciaForm(request.POST)
        if form.is_valid():
            competencia = form.save()
            return redirect('competencia_detail', pk=competencia.pk)
    else:
        form = CompetenciaForm()
    return render(request, 'competencias/competencia_edit.html', {'form': form})
# competencias/views.py
def competencia_edit(request, pk):
    competencia = get_object_or_404(Competencia, pk=pk)
    if request.method == "POST":
        form = CompetenciaForm(request.POST, instance=competencia)
        if form.is_valid():
            competencia = form.save()
            return redirect('competencia_detail', pk=competencia.pk)
    else:
        form = CompetenciaForm(instance=competencia)
    return render(request, 'competencias/competencia_edit.html', {'form': form})
# competencias/views.py
def competencia_delete(request, pk):
    competencia = get_object_or_404(Competencia, pk=pk)
    if request.method == 'POST':
        competencia.delete()
        return redirect('competencia_list')
    return render(request, 'competencias/competencia_delete.html', {'competencia': competencia})
