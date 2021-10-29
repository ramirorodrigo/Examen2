from django.contrib import admin

from .models import Procesos, Prestamo, Devolucion

admin.site.register([Procesos, Prestamo, Devolucion])