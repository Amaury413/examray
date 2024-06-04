# views.py
from django.shortcuts import render, redirect
from .models import Proyecto, Tarea
from .forms import ProyectoForm, TareaForm

def lista_proyectos(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'lista_proyectos.html', {'proyectos': proyectos})

def crear_proyecto(request):
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_proyectos')
    else:
        form = ProyectoForm()
    return render(request, 'crear_proyecto.html', {'form': form})

def lista_tareas(request):
    tareas = Tarea.objects.all()
    return render(request, 'lista_tareas.html', {'tareas': tareas})

def crear_tarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_tareas')
    else:
        form = TareaForm()
    return render(request, 'crear_tarea.html', {'form': form})
