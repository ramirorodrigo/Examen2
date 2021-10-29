from django.contrib import admin

from .models import Usuario, Bibliotecario, Lector

admin.site.register([Usuario, Bibliotecario, Lector])
