from django.shortcuts import render

from django.shortcuts import HttpResponse, render

def index (request):
    
    return render(request, 'AppConsultoria/index.html')

def servicios (request):
    
    return render(request, 'AppConsultoria/servicios.html')


def consultores (request):
    
    return render(request, 'AppConsultoria/consultores.html')

def publicaciones (request):
    
    return render(request, 'AppConsultoria/publicaciones.html')

def clientes (request):
    
    return render(request, 'AppConsultoria/clientes.html')


def formulario(request):
    
    return render(request, "AppConsultoria/formulario.html")