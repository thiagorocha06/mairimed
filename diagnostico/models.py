from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext as _
from django.conf import settings

from dieta.models import Dieta
from medicamento.models import Medicamento
from sintoma.models import Sintoma
from recomendacao.models import Recomendacao

class Diagnostico(models.Model):
    diagnostico = models.CharField(max_length=50)
    sintomas = models.ManyToManyField(Sintoma, verbose_name="Sintoma")
    recomendacoes = models.ManyToManyField(Recomendacao, blank=True)
    medicamentos = models.ManyToManyField(Medicamento, blank=True)

    class Meta:
        verbose_name = _("Diagnostico")
        verbose_name_plural = _("Diagnosticos")

    def __str__(self):
        return self.diagnostico
