from django.db import models

class Consultor(models.Model):
    
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    carrera=models.CharField(max_length=40)
    salario=models.FloatField()
    
    def __str__(self):
        return f'Nombre consultor:{self.nombre} {self.apellido}, especialidad: {self.carrera}'
    
    
class Clientes(models.Model):
    
    empresa=models.CharField(max_length=20)
    rubro=models.CharField(max_length=20)
    fecha_ingreso=models.DateField()
    proyectos = models.CharField(max_length=20)
    
    def __str__(self):
        return f'Cliente: {self.empresa}, desde el  ==> {self.fecha_ingreso}'
    
class Servicios(models.Model):
    nombre_servicio=models.CharField(max_length=20)
    descripcion=models.CharField(max_length=200)
    precio=models.FloatField()
    
    def __str__(self):
        return f'Servicio: {self.nombre_servicio}, precio ==>{self.precio}'
    
    
class PublicacionesAcademicas(models.Model):
    nombre=models.CharField(max_length=40)
    fecha=models.DateField()
    agencia=models.FloatField()
    descripcion=models.CharField(max_length=200)

    def __str__(self):
        return f'Publicacion {self.nombre}, en {self.fecha}, revista: {self.agencia}'