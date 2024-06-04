from django.db import models
from django.contrib.auth.models import User

class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nombre

class Tarea(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('en_progreso', 'En Progreso'),
        ('completada', 'Completada'),
    ]

    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    estado = models.CharField(max_length=50, choices=ESTADO_CHOICES, default='pendiente')
    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_limite = models.DateField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo