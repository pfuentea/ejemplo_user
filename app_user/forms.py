from django import forms
from .models import Usuario , Propiedad

class UsuarioForms(forms.ModelForm):
    class Meta:
        model=Usuario
        fields =['username','email','first_name','last_name','rut']

class PropiedadForm(forms.ModelForm):
    class Meta:
        model=Propiedad
        fields =['nombre']

