from django.contrib import admin
from AppCoder.models import Consultor, Clientes, Servicios, PublicacionesAcademicas 

# Register your models here.

admin.site.register(Consultor)
admin.site.register(Clientes)
admin.site.register(Servicios)
admin.site.register(PublicacionesAcademicas)