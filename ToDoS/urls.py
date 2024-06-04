# urls.py
from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.lista_proyectos, name='lista_proyectos'),
    path('proyectos/crear/', views.crear_proyecto, name='crear_proyecto'),
    path('tareas/', views.lista_tareas, name='lista_tareas'),
    path('tareas/crear/', views.crear_tarea, name='crear_tarea'),
]
