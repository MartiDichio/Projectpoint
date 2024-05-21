from django.shortcuts import render

from .models import Monoambiente, UnDormitorio, DosDormitorios
from .forms import MonoambienteForm, UnDormitorioForm, DosDormitoriosForm

def index(request):
    
    return render(request, 'index.html')

def crear_monoambiente(request):
    if request.method == 'POST':
        form = MonoambienteForm(request.POST)
        if form.is_valid():
            form.save()
            
    else:
        form = MonoambienteForm()
    return render(request, 'crear_monoambiente.html', {'form': form})

def crear_un_dormitorio(request):
    
    return render(request, 'crear_un_dormitorio.html')

def crear_dos_dormitorios(request):
    
    return render(request, 'crear_dos_dormitorios.html')


# Create your views here.
