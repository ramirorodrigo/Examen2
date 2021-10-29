from django.db import models

from administracion.models import Bibliotecario, Lector
from Adquisicion.models import Libros


class Procesos(models.Model):
    detalle = models.CharField(max_length=77, help_text='Intrusca el detalle', null=True, blank=True)
    libro = models.OneToOneField(Libros, on_delete=models.CASCADE)
    bibliotecario = models.OneToOneField(Bibliotecario, on_delete=models.CASCADE, null=True, blank=True)
    lector = models.OneToOneField(Lector, on_delete=models.CASCADE, null=True, blank=True)
    fecha = models.DateTimeField()

    class Meta:
        ordering = ['-fecha']


class Prestamo(models.Model):
    item_prestamo = models.CharField(max_length=7, unique=True)
    proceso_id = models.OneToOneField(Procesos, on_delete=models.CASCADE, null=True, blank=True)
    fecha_pres = models.DateTimeField()
    

    def __str__(self):
        return self.item_prestamo

class Devolucion(models.Model):
    item_devolucion = models.CharField(max_length=7, unique=True)
    proceso_id = models.OneToOneField(Procesos, on_delete=models.CASCADE, null=True, blank=True)
    fecha_dev = models.DateTimeField()
    

    def __str__(self):
        return self.item_devolucion
