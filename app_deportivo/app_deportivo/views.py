from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy




def index(request):
    return render(request, 'index.html')

