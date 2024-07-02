# categorias/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Categoria

def categoria_list(request):
    categorias = Categoria.objects.all()
    return render(request, 'categorias/categoria_list.html', {'categorias': categorias})
# categorias/views.py
def categoria_detail(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    return render(request, 'categorias/categoria_detail.html', {'categoria': categoria})
# categorias/views.py
def categoria_new(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            categoria = form.save()
            return redirect('categoria_detail', pk=categoria.pk)
    else:
        form = CategoriaForm()
    return render(request, 'categorias/categoria_edit.html', {'form': form})
# categorias/views.py
def categoria_edit(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == "POST":
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            categoria = form.save()
            return redirect('categoria_detail', pk=categoria.pk)
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'categorias/categoria_edit.html', {'form': form})
# categorias/views.py
def categoria_delete(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        categoria.delete()
        return redirect('categoria_list')
    return render(request, 'categorias/categoria_delete.html', {'categoria': categoria})
