from django.shortcuts import render

from .models import Monoambiente, UnDormitorio, DosDormitorios
from .forms import MonoambienteForm, UnDormitorioForm, DosDormitoriosForm

def index(request):
    # Define la lógica de la vista principal (por ejemplo, una lista de departamentos)
    return render(request, 'index.html')

def crear_monoambiente(request):
    if request.method == 'POST':
        form = MonoambienteForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirige a alguna página de éxito o muestra un mensaje de éxito
    else:
        form = MonoambienteForm()
    return render(request, 'crear_monoambiente.html', {'form': form})

def crear_un_dormitorio(request):
    # Define la lógica para crear un departamento de un dormitorio
    return render(request, 'crear_un_dormitorio.html')

def crear_dos_dormitorios(request):
    # Define la lógica para crear un departamento de dos dormitorios
    return render(request, 'crear_dos_dormitorios.html')


# Create your views here.
