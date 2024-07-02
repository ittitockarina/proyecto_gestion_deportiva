# deportes/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Deporte


def deporte_list(request):
    deportes = Deporte.objects.all()
    return render(request, 'deportes/deporte_list.html', {'deportes': deportes})
# deportes/views.py
def deporte_detail(request, pk):
    deporte = get_object_or_404(Deporte, pk=pk)
    return render(request, 'deportes/deporte_detail.html', {'deporte': deporte})
# deportes/views.py
def deporte_new(request):
    if request.method == "POST":
        form = DeporteForm(request.POST)
        if form.is_valid():
            deporte = form.save()
            return redirect('deporte_detail', pk=deporte.pk)
    else:
        form = DeporteForm()
    return render(request, 'deportes/deporte_edit.html', {'form': form})
# deportes/views.py
def deporte_edit(request, pk):
    deporte = get_object_or_404(Deporte, pk=pk)
    if request.method == "POST":
        form = DeporteForm(request.POST, instance=deporte)
        if form.is_valid():
            deporte = form.save()
            return redirect('deporte_detail', pk=deporte.pk)
    else:
        form = DeporteForm(instance=deporte)
    return render(request, 'deportes/deporte_edit.html', {'form': form})
# deportes/views.py
def deporte_delete(request, pk):
    deporte = get_object_or_404(Deporte, pk=pk)
    if request.method == 'POST':
        deporte.delete()
        return redirect('deporte_list')
    return render(request, 'deportes/deporte_delete.html', {'deporte': deporte})
