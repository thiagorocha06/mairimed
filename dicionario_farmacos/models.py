from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext as _

class Farmaco(models.Model):
    data_de_criacao = models.DateTimeField(default=timezone.now)
    data_de_publicacao = models.DateTimeField(blank=True, null=True)
    nome = models.CharField(max_length=200, blank=False)
    introducao = models.TextField(max_length=1000, blank=True, null=True, help_text=_("introducao"))
    indicacoes = models.TextField(max_length=1000, blank=True, null=True, help_text=_("indicacoes"))
    farmacodinamica = models.TextField(max_length=1000, blank=True, null=True, help_text=_("farmacodinamica"))
    farmacocinetica = models.TextField(max_length=1000, blank=True, null=True, help_text=_("farmacocinetica"))
    contraindicacoes = models.TextField(max_length=1000, blank=True, null=True, help_text=_("contraindicacoes"))
    precaucoes = models.TextField(max_length=1000, blank=True, null=True, help_text=_("precaucoes"))
    gravidez = models.TextField(max_length=1000, blank=True, null=True, help_text=_("gravidez"))
    lactacao = models.TextField(max_length=1000, blank=True, null=True, help_text=_("lactacao"))
    posologia = models.TextField(blank=True, null=True, help_text=_("posologia"))
    pediatria = models.TextField(blank=True, null=True, help_text=_("pediatria"))
    reacoes = models.TextField(max_length=1000, blank=True, null=True, help_text=_("reacoes"))
    texto = models.TextField(blank=True, null=True, help_text=_("texto acessorio"))

    url = models.SlugField(
        max_length=60, blank=False, null=True,
        help_text=_("a user friendly url"),
        verbose_name=_("user friendly url"))

    def __str__(self):
        return self.nome
