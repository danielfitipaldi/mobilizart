from django.db import models
from django import forms


class Categoria(models.Model):
    nome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    def __str__(self):
        return self.nome



