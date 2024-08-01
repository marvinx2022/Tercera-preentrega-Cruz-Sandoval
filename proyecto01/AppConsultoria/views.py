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

from AppConsultoria.forms import formulario_consultor, formulario_cliente, formulario_servicio, formulario_publicacion, PublicacionesAcademicasSearchForm
from AppConsultoria.models import Consultor, Clientes, Servicios, PublicacionesAcademicas
 
def crear_consultor(request):
 
      if request.method == "POST":
 
            miFormulario = formulario_consultor(request.POST) 
            print(miFormulario)
 
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  nombre = Consultor(nombre=informacion["nombre"], apellido=informacion["apellido"], carrera = informacion["carrera"], salario = informacion["salario"])
                  nombre.save()
                  return render(request, "AppConsultoria/index.html")
      else:
            miFormulario = formulario_consultor()
 
      return render(request, "AppConsultoria/crear_consultor.html", {"miFormulario": miFormulario})
  
  
def crear_cliente(request):
 
      if request.method == "POST":
 
            miFormulario = formulario_cliente(request.POST) 
            print(miFormulario)
 
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  nombre = Clientes(empresa=informacion["empresa"], rubro=informacion["rubro"], fecha_ingreso = informacion["fecha_ingreso"], proyectos = informacion["proyectos"])
  
                  nombre.save()
                  return render(request, "AppConsultoria/index.html")
      else:
            miFormulario = formulario_cliente()
 
      return render(request, "AppConsultoria/crear_cliente.html", {"miFormulario": miFormulario})
  
  
  
def crear_servicio(request):
 
      if request.method == "POST":
 
            miFormulario = formulario_servicio(request.POST) 
            print(miFormulario)
 
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  nombre = Servicios(nombre_servicio=informacion["nombre_servicio"], descripcion=informacion["descripcion"], precio = informacion["precio"])
  

                  nombre.save()
                  return render(request, "AppConsultoria/index.html")
      else:
            miFormulario = formulario_servicio()
 
      return render(request, "AppConsultoria/crear_servicio.html", {"miFormulario": miFormulario})
  
def crear_publicacion(request):
 
      if request.method == "POST":
 
            miFormulario = formulario_publicacion(request.POST) 
            print(miFormulario)
 
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  nombre = PublicacionesAcademicas(nombre=informacion["nombre"], fecha=informacion["fecha"], agencia = informacion["agencia"], descripcion = informacion["descripcion"])
  

                  nombre.save()
                  return render(request, "AppConsultoria/index.html")
      else:
            miFormulario = formulario_publicacion()
 
      return render(request, "AppConsultoria/crear_publicacion.html", {"miFormulario": miFormulario})
  
  
def buscar_publicaciones(request):
    
    form = PublicacionesAcademicasSearchForm(request.GET)
    publicaciones = []
    if form.is_valid():
        nombre = form.cleaned_data.get('nombre')
        fecha = form.cleaned_data.get('fecha')
        agencia = form.cleaned_data.get('agencia')
        descripcion = form.cleaned_data.get('descripcion')

        publicaciones = PublicacionesAcademicas.objects.all()

        if nombre:
            publicaciones = publicaciones.filter(nombre__icontains=nombre)
        if fecha:
            publicaciones = publicaciones.filter(fecha=fecha)
        if agencia:
            publicaciones = publicaciones.filter(agencia=agencia)
        if descripcion:
            publicaciones = publicaciones.filter(descripcion__icontains=descripcion)

    return render(request, 'AppConsultoria/buscar_publicacion.html', {'form': form, 'publicaciones': publicaciones})