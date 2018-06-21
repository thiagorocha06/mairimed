from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext as _

class Doenca(models.Model):
    data_de_criacao = models.DateTimeField(default=timezone.now)
    data_de_publicacao = models.DateTimeField(blank=True, null=True)
    nome = models.CharField(max_length=200, blank=False)
    introducao = models.TextField(max_length=1000, blank=True, null=True)
    manifestacoes = models.TextField(max_length=1000, blank=True, null=True)
    exames = models.TextField(max_length=1000, blank=True, null=True)
    diagnostico = models.TextField(max_length=1000, blank=True, null=True)
    tratamento = models.TextField(max_length=1000, blank=True, null=True, help_text=_("objetivos do tratamento"), verbose_name=_("objetivos do tratamento"))
    prescricao = models.TextField(blank=True, null=True)
    texto = models.TextField(blank=True, null=True)

    url = models.SlugField(
        max_length=60, blank=False, null=True,
        help_text=_("a user friendly url"),
        verbose_name=_("user friendly url"))

    def __str__(self):
        return self.nome
