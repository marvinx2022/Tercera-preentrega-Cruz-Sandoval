from django import forms

class formulario_consultor(forms.Form):
    
    nombre = forms.CharField()
    apellido = forms.CharField() 
    carrera = forms.CharField()
    salario = forms.FloatField()
    
    
class formulario_cliente(forms.Form):
    
    empresa=forms.CharField()
    rubro=forms.CharField()
    fecha_ingreso = forms.DateField(
        label='Fecha',
        widget=forms.DateInput(attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d']  
    )
    proyectos = forms.CharField()
    
class formulario_servicio(forms.Form):
    
    nombre_servicio=forms.CharField()
    descripcion=forms.CharField()
    precio=forms.FloatField()
    
class formulario_publicacion(forms.Form):
    
    nombre=forms.CharField()
    fecha=forms.DateField(
        label='Fecha',
        widget=forms.DateInput(attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d']  
    )
    agencia=forms.FloatField()
    descripcion=forms.CharField()
    
class PublicacionesAcademicasSearchForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=40, required=False)
    fecha = forms.DateField(label='Fecha', required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    agencia = forms.FloatField(label='Agencia', required=False)
    descripcion = forms.CharField(label='Descripción', max_length=200, required=False)
    
    