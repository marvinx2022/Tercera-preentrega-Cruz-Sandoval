from django.db import models

class Curso(models.Model):
    
    nombre=models.CharField(max_length=40)
    camada=models.IntegerField()
    duracion=models.IntegerField()
    precio=models.FloatField()
    
    def __str__(self):
        return f'Nombre curso:{self.nombre}, dura: {self.duracion}, costo: {self.costo}'
    
    
class Profesores(models.Model):
    
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    camada=models.IntegerField()
    curso = models.CharField(max_length=20)
    
    def __str__(self):
        return f'Profesor: {self.nombre} {self.apellido}, asignado al curso ==>{self.curso}'
    
class Alumnos(models.Model):
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=40)
    dni=models.IntegerField()
    
    def __str__(self):
        return f'Estudiante: {self.nombre} {self.apellido}, cursando ==>{self.curso}'
    
    
class Carreras(models.Model):
    nombre=models.CharField(max_length=20)
    duracion=models.IntegerField()
    precio=models.FloatField()

    def __str__(self):
        return f'Carrera {self.nombre} duración {self.duracion}'