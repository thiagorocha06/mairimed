from django.db import models
from django.utils.translation import ugettext_lazy as _

class Recomendacao(models.Model):
    recomendacao = models.CharField(max_length=200)

    class Meta:
        verbose_name = _("Recomendacao")
        verbose_name_plural = _("Recomendacoes")

    def __str__(self):
        return self.recomendacao
