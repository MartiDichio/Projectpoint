from django import forms
from .models import Monoambiente, UnDormitorio, DosDormitorios

class MonoambienteForm(forms.ModelForm):
    class Meta:
        model = Monoambiente
        fields = ['nombre', 'metros_cuadrados', 'precio', 'ubicacion', 'vista']

class UnDormitorioForm(forms.ModelForm):
    class Meta:
        model = UnDormitorio
        fields = ['nombre', 'metros_cuadrados', 'precio', 'ubicacion', 'vista']

class DosDormitoriosForm(forms.ModelForm):
    class Meta:
        model = DosDormitorios
        fields = ['nombre', 'metros_cuadrados', 'precio', 'ubicacion', 'vista']
