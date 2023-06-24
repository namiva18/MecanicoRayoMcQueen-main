from django import forms
from .models import Contacto, Publicacion

class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ('titulo', 'contenido','imagen')


class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'correo', 'telefono', 'mensaje']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Ingresa tu nombre'}),
            'correo': forms.EmailInput(attrs={'placeholder': 'Ingresa tu correo electrónico'}),
            'telefono': forms.TextInput(attrs={'placeholder': 'Ingresa tu número telefónico'}),
            'mensaje': forms.Textarea(attrs={'placeholder': 'Escribe tu mensaje aquí'}),
        }