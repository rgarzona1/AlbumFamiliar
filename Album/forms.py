from django import forms
from .models import Fotos

class FotoForm(forms.ModelForm):
    class Meta:
        model = Fotos
        fields = ['titulo', 'descripcion', 'fecha', 'imagen']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Título de la foto'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Descripción de la foto',
                'rows': 3
            }),
            'fecha': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'imagen': forms.ClearableFileInput(attrs={
                'class': 'form-control-file'
            }),
        }
        labels = {
            'titulo': 'Título',
            'descripcion': 'Descripción',
            'fecha': 'Fecha',
            'imagen': 'Seleccionar imagen'
        }
