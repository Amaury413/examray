# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
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

def actualizar_proyecto(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk)
    if request.method == 'POST':
        form = ProyectoForm(request.POST, instance=proyecto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Proyecto actualizado con éxito.')
            return redirect('lista_proyectos')
        else:
            messages.error(request, 'Error al actualizar el proyecto. Por favor, revisa el formulario.')
    else:
        form = ProyectoForm(instance=proyecto)
    return render(request, 'crear_proyecto.html', {'form': form})

def eliminar_proyecto(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk)
    if request.method == 'POST':
        proyecto.delete()
        messages.success(request, 'Proyecto eliminado con éxito.')
        return redirect('lista_proyectos')
    return render(request, 'confirmar_eliminacion.html', {'obj': proyecto})

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

def actualizar_tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    if request.method == 'POST':
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tarea actualizada con éxito.')
            return redirect('lista_tareas')
        else:
            messages.error(request, 'Error al actualizar la tarea. Por favor, revisa el formulario.')
    else:
        form = TareaForm(instance=tarea)
    return render(request, 'crear_tarea.html', {'form': form})

def eliminar_tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    if request.method == 'POST':
        tarea.delete()
        messages.success(request, 'Tarea eliminada con éxito.')
        return redirect('lista_tareas')
    return render(request, 'confirmar_eliminacion.html', {'obj': tarea})