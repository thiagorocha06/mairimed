from django.db import models
from django.utils.translation import ugettext_lazy as _

class Medicamento(models.Model):
     medicamento = models.CharField(max_length=200)

     class Meta:
         verbose_name = _("Medicamento")
         verbose_name_plural = _("Medicamentos")

     def __str__(self):
         return self.medicamento
