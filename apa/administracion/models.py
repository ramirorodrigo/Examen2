from django.db import models
from django.db.models.base import Model

class Usuario(models.Model):
    ci = models.CharField(max_length=10, unique=True, help_text='Introdusca el número CI')
    nombres = models.CharField(max_length=20, help_text='Intrusca nombres')
    apellidos = models.CharField(max_length=20, help_text='Intrusca apellidos')
    direccion = models.CharField(max_length=20, help_text='Intrusca direccion', null=True, blank=True)
    fecha = models.DateTimeField()

    def __str__(self):
        return self.nombres + ' ' + self.apellidos 

    class Meta:
        ordering = ['-apellidos', 'nombres']


class Lector(models.Model):
    item_lector = models.CharField(max_length=7, unique=True)
    usuario_id = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.item_lector

class Bibliotecario(models.Model):
    item_bibli = models.CharField(max_length=7, unique=True)
    usuario_id = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.item_bibli