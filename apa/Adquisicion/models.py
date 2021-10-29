from django.db import models
from django.db.models.base import Model

class Libros(models.Model):
    titulo_de_libro = models.CharField(max_length=77, help_text='introdusca titulo de Libro')
    autor = models.CharField(max_length=20, help_text='Intrusca nombre de Autor')
    editorial = models.CharField(max_length=20, help_text='Intrusca editorial', null=True, blank=True)
    fecha = models.DateTimeField()

    def __str__(self):
        return self.titulo_de_libro + ' ' + self.autor

    class Meta:
        ordering = ['-titulo_de_libro']
