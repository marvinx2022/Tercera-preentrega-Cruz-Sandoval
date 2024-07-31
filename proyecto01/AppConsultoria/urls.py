from django.urls import path
from AppCoder import views

from django.conf import settings
from django.conf.urls.static import static

from AppConsultoria.views import index, consultores, servicios, publicaciones, formulario, clientes
from django.contrib import admin
from django.urls import path

urlpatterns = [
    
    path('index/', index, name='Index'),
    path('servicios/', servicios, name='Servicios'),
    path('consultores/', consultores, name='Consultores'),
    path('publicaciones/', publicaciones, name='Publicaciones'),
    path('clientes/', clientes, name='Clientes'),
    path('formulario/', formulario, name='Formulario')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)