from django.db import models
from django.utils.translation import ugettext as _

class Farmaco(models.Model):
    nome = models.CharField(max_length=200, blank=False)
    introducao = models.TextField(max_length=1000, blank=True, null=True)
    indicacoes = models.TextField(max_length=1000, blank=True, null=True)
    farmacodinamica = models.TextField(max_length=1000, blank=True, null=True)
    farmacocinetica = models.TextField(max_length=1000, blank=True, null=True)
    contraindicacoes = models.TextField(max_length=1000, blank=True, null=True)
    precaucoes = models.TextField(max_length=1000, blank=True, null=True)
    gravidez = models.TextField(max_length=1000, blank=True, null=True)
    lactacao = models.TextField(max_length=1000, blank=True, null=True)
    interacoes = models.TextField(max_length=1000, blank=True, null=True)
    posologia = models.TextField(blank=True, null=True)
    pediatria = models.TextField(blank=True, null=True)
    reacoes = models.TextField(max_length=1000, blank=True, null=True)
    texto = models.TextField(blank=True, null=True)

    url = models.SlugField(
        max_length=60, blank=False, null=True,
        help_text=_("a user friendly url"),
        verbose_name=_("user friendly url"))

    def __str__(self):
        return self.nome
