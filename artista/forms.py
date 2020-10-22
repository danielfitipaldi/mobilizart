from django import forms
from .models import Artista


class FormArtista(forms.ModelForm):
    class Meta:
        model = Artista
        exclude = ('data_criacao',)



