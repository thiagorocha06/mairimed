from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext as _
from model_utils.managers import InheritanceManager

@python_2_unicode_compatible
class Instituicao(models.Model):

    instituicao = models.CharField(
        verbose_name=_("Instituicao"),
        max_length=250, blank=True, null=True)

    class Meta:
        verbose_name = _("Instituicao")
        verbose_name_plural = _("Instituicao")

    def __str__(self):
        return self.instituicao

class Link(models.Model):
    nome = models.CharField(max_length=200, blank=False)
    link = models.CharField(max_length=200, help_text=_("link"))
    instituicao = models.ForeignKey(
        Instituicao, null=True, blank=True,
        verbose_name=_("Instituicao"), on_delete=models.CASCADE,)

    def __str__(self):
        return self.nome
