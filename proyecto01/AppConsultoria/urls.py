from django.urls import path
from AppCoder import views

from django.conf import settings
from django.conf.urls.static import static

from AppConsultoria.views import index, consultores, servicios, publicaciones, clientes, crear_consultor, crear_cliente, crear_servicio, crear_publicacion, buscar_publicaciones
from django.contrib import admin
from django.urls import path

urlpatterns = [
    
    path('index/', index, name='Index'),
    path('servicios/', servicios, name='Servicios'),
    path('consultores/', consultores, name='Consultores'),
    path('publicaciones/', publicaciones, name='Publicaciones'),
    path('clientes/', clientes, name='Clientes'),
    path('crear_consultor/', crear_consultor, name='Crear_consultor'),
    path('crear_cliente/', crear_cliente, name='Crear_cliente'),
    path('crear_servicio/', crear_servicio, name='Crear_servicio'),
    path('crear_publicacion/', crear_publicacion, name='Crear_publicacion'),
    path('buscar_publicacion/', buscar_publicaciones, name='Buscar_publicaciones')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)