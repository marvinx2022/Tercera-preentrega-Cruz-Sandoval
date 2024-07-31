from django import forms

class formulario_consultor(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField() 