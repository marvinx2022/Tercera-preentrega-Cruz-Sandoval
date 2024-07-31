from django.contrib import admin

from AppConsultoria.models import Consultor, Clientes, Servicios, PublicacionesAcademicas 


admin.site.register(Consultor)
admin.site.register(Clientes)
admin.site.register(Servicios)
admin.site.register(PublicacionesAcademicas)