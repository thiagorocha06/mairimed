from django.db import models
from django.utils.translation import ugettext as _

class Alimento(models.Model):
    nome = models.CharField(max_length=200, blank=False)
    tipo = models.CharField(max_length=200, blank=True, null=True)
    nome_cientifico = models.CharField(max_length=200, blank=True, help_text=_("nome cientifico"))
    nomes_populares = models.CharField(max_length=500, blank=True, help_text=_("nomes populares"))
    componentes  = models.TextField(max_length=500, blank=True, help_text=_("componentes"))
    tabela_nutricional  = models.TextField(blank=True, help_text=_("tabela nutricional"))
    beneficios  = models.TextField(max_length=500, blank=True, help_text=_("beneficios"))
    consumo  = models.TextField(max_length=500, blank=True, help_text=_("consumo"))
    texto = models.TextField(blank=True, null=True, help_text=_("texto acessorio"))

    url = models.SlugField(
        max_length=60, blank=False, null=True,
        help_text=_("a user friendly url"),
        verbose_name=_("user friendly url"))

    def __str__(self):
        return self.nome
