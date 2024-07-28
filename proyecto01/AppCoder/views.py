from django.shortcuts import HttpResponse, render

def estudiantes (request):
    
    return render(request, 'ApCoder/estudiantes.html')

def profesores (request):
    
    return render(request, 'AppCoder/profesores.html')

def main (request):
    
    return render(request, 'AppCoder/main.html')

def cursos (request):
    
    return render(request, 'AppCoder/cursos.html')



