from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

class Sintoma(models.Model):
    sintoma = models.CharField(max_length=30)
    descricao = models.CharField(max_length=100)

    class Meta:
        verbose_name = _("Sintoma")
        verbose_name_plural = _("Sintomas")

    def __str__(self):
        return self.sintoma
