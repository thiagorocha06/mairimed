from django.db import models
from django.utils.translation import ugettext as _

class Alimento(models.Model):
    nome = models.CharField(max_length=200, blank=False)
    tipo = models.CharField(max_length=200, blank=True, null=True)
    texto = models.TextField(blank=True, null=True)

    url = models.SlugField(
        max_length=60, blank=False, null=True,
        help_text=_("a user friendly url"),
        verbose_name=_("user friendly url"))

    def __str__(self):
        return self.nome
