from django.http import HttpResponse
from django.template import loader, Template, context


def saludo (request):
    
    return HttpResponse('Hola, este es un saludo')


def mejor_saludo(request):
    
    return HttpResponse('Este es un saludo mejor')

def saludar_por_nombre(self, nombre):
    
    saludo_a_mostrar=f'Hola estimado {nombre}, te mando un atento y cordial saludo'
    
    return HttpResponse(saludo_a_mostrar)

def probando_template(self):
    
    nom='Marvin'
    ap='Cruz'
    
    diccionario= {'nombre':nom,'apellido':ap}
    
    plantilla=loader.get_template('index.html')
    
    documento=plantilla.render(diccionario)
    
    return HttpResponse(documento)
    
def load_about(self):
    
    acerca_de_mi= {'Nombre':'Marvin','Apellido':'Cruz','Edad':'39'}
    
    plantilla=loader.get_template('about.html')
    
    documento=plantilla.render(acerca_de_mi)
     
    