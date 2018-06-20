from django.db import models
from django.utils.translation import ugettext as _

class Doenca(models.Model):
    nome = models.CharField(max_length=200, blank=False)
    introducao = models.TextField(max_length=50, blank=True, null=True)
    manifestacoes = models.TextField(max_length=50, blank=True, null=True)
    exames = models.TextField(max_length=50, blank=True, null=True)
    tratamento = models.TextField(max_length=50, blank=True, null=True)

    url = models.SlugField(
        max_length=60, blank=False, null=True,
        help_text=_("a user friendly url"),
        verbose_name=_("user friendly url"))

    def __str__(self):
        return self.nome
