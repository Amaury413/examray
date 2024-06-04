from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Tarea, Proyecto

admin.site.register(Tarea)
admin.site.register(Proyecto)
