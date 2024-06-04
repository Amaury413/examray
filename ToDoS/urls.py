from django.urls import path
from .views import (
    lista_proyectos, crear_proyecto, actualizar_proyecto, eliminar_proyecto,
    lista_tareas, crear_tarea, actualizar_tarea, eliminar_tarea, Proyecto
)

urlpatterns = [
    path('proyectos/', lista_proyectos, name='lista_proyectos'),
    path('proyectos/crear/', crear_proyecto, name='crear_proyecto'),
    path('proyectos/actualizar/<int:pk>/', actualizar_proyecto, name='actualizar_proyecto'),
    path('proyectos/eliminar/<int:pk>/', eliminar_proyecto, name='eliminar_proyecto'),
    path('tareas/', lista_tareas, name='lista_tareas'),
    path('tareas/crear/', crear_tarea, name='crear_tarea'),
    path('tareas/actualizar/<int:pk>/', actualizar_tarea, name='actualizar_tarea'),
    path('tareas/eliminar/<int:pk>/', eliminar_tarea, name='eliminar_tarea'),
]
