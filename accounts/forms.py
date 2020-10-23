from django import forms
from .models import Categoria


class FormCategoria(forms.ModelForm):
    class Meta:
        model = Categoria
        exclude = ()



