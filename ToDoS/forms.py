# forms.py
from django import forms
from .models import Proyecto, Tarea

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['nombre', 'descripcion', 'fecha_inicio', 'fecha_fin']

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'estado', 'fecha_limite', 'usuario', 'proyecto']
