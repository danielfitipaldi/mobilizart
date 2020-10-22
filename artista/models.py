from django.db import models
from django.utils import timezone
from accounts.models import Categoria
from django import forms


class Artista(models.Model):
    nome = models.CharField(
        max_length=255,
        blank=False,
        null=False
    )

    sobrenome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    data_nascimento = models.DateField()

    data_criacao = models.DateTimeField(
        default=timezone.now
    )

    cpf = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        help_text='Apenas números'
    )

    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('NB', 'Não Binário')
    )
    genero = models.CharField(max_length=2, choices=GENDER_CHOICES)

    bairro = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    cidade = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    estado = models.CharField(
        max_length=2,
        choices=(('AC', 'Acre'),
                 ('AL', 'Alagoas'),
                 ('AP', 'Amapá'),
                 ('AM', 'Amazonas'),
                 ('BA', 'Bahia'),
                 ('CE', 'Ceará'),
                 ('DF', 'Distrito Federal'),
                 ('ES', 'Espírito Santo'),
                 ('GO', 'Goiás'),
                 ('MA', 'Maranhão'),
                 ('MT', 'Mato Grosso'),
                 ('MS', 'Mato Grosso do Sul'),
                 ('MG', 'Minas Gerais'),
                 ('PA', 'Pará'),
                 ('PB', 'Paraíba'),
                 ('PR', 'Paraná'),
                 ('PE', 'Pernambuco'),
                 ('PI', 'Piauí'),
                 ('RJ', 'Rio de Janeiro'),
                 ('RN', 'Rio Grande do Norte'),
                 ('RS', 'Rio Grande do Sul'),
                 ('RO', 'Rondônia'),
                 ('RR', 'Roraima'),
                 ('SC', 'Santa Catarina'),
                 ('SP', 'São Paulo'),
                 ('SE', 'Sergipe'),
                 ('TO', 'Tocantins'),
                 ))

    pais = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    email = models.CharField(
        max_length=255,
        blank=False,
        null=False,
    )

    categoria = models.ForeignKey(
        Categoria, on_delete=models.DO_NOTHING,
        help_text='Escolha apenas uma categoria'
    )

    sobre = models.TextField(
        blank=True
    )

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'


class FormArtista(forms.ModelForm):
    class Meta:
        model = Artista
        exclude = ('data_criacao',)
