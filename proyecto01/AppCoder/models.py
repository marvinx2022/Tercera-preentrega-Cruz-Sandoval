from django.db import models

# Create your models here.

class Curso(models.Model):
    
    nombre=models.CharField(max_length=40)
    camada=models.IntegerField()
    
class Profesores(models.Model):
    
    nombre=models.CharField(max_length=20)
    camada=models.IntegerField()
    
    
class Alumnos(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=75)
    dni=models.IntegerField()