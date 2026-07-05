from django.db import models
from appFacultad.models import Facultad
# Create your models here.
class Carrera(models.Model):
    nombre_carrera = models.CharField(max_length=100)
    code = models.CharField(max_length=15, unique=True)
    facultad = models.ForeignKey(
        Facultad,
        on_delete=models.CASCADE,
        related_name='carreras',
        blank=True,
        null=True,
    )
    
    def __str__(self):
        return self.nombre_carrera
