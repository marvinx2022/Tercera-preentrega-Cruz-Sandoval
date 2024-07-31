from django.urls import path
from AppCoder import views

from django.conf import settings
from django.conf.urls.static import static

from AppCoder.views import estudiantes, profesores, main, cursos
from django.contrib import admin
from django.urls import path

urlpatterns = [
    
    path('main/', main, name='Main'),
    path('estudiantes/', estudiantes, name='Estudiantes'),
    path('profesores/', profesores, name='Profesores'),
    path('cursos/', cursos, name='Cursos')

    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)