from django.urls import path
from AppCoder import views

from AppCoder.views import estudiantes, profesores, main, cursos
from django.contrib import admin
from django.urls import path

urlpatterns = [
    
    path('estudiantes/', estudiantes, name='Estudiantes'),
    path('profesores/', profesores, name='Profesores'),
    path('main/', main, name='Main'),
    path('cursos/', cursos, name='Cursos')

    
]
