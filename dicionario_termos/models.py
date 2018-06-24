from django.db import models
from django.utils.translation import ugettext as _

class Termo(models.Model):
    nome = models.CharField(max_length=200, blank=False)
    tipo = models.CharField(max_length=200, blank=True, null=True, help_text=_("tipo"))
    origem = models.TextField(max_length=50, blank=True, null=True, help_text=_("origem"))
    definicao = models.TextField(blank=True, null=True, help_text=_("definicao"))
    texto = models.TextField(blank=True, null=True, help_text=_("texto acessorio"))

    url = models.SlugField(
        max_length=60, blank=False, null=True,
        help_text=_("a user friendly url"),
        verbose_name=_("user friendly url"))

    def __str__(self):
        return self.nome
