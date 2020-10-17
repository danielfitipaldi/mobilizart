from django.db import models
from django.utils import timezone
from accounts.models import Categoria


class Usuario(models.Model):
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

    cpf = models.CharField(max_length=255, blank=False, null=False)

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
        max_length=255,
        null=False,
        blank=False
    )

    pais = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    email = models.CharField(
        max_length=255,
        blank=False,
        null=False
    )

    categoria = models.ForeignKey(
        Categoria, on_delete=models.DO_NOTHING
    )

    sobre = models.TextField(
        blank=True
    )

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'
