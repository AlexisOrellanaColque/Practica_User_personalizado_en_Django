from django.db import models
from appCarrera.models import Carrera

# Create your models here.

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    codigo_estudiante = models.CharField(max_length=15, unique=True)
    carrera = models.ForeignKey(
        Carrera,
        on_delete=models.CASCADE,
        related_name= 'estudiantes',
        blank=True,
        null=True
        
        
    )
    
    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.codigo_estudiante})"