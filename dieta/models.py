from django.db import models
from django.utils.translation import ugettext as _
from django.utils import timezone
from django.conf import settings

class Alimento(models.Model):
    nome = models.CharField(max_length=30)
    porcao = models.DecimalField(max_digits=5, decimal_places=1, default=1)
    unidade = models.CharField(max_length=30)
    quantidade = models.DecimalField(max_digits=3, decimal_places=0, default=1)
    calorias = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2)

    def __str__(self):
        return self.nome+' '+str(self.porcao)+' '+self.unidade

class Dieta(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    nome_dieta = models.CharField(max_length=30)
    descricao = models.CharField(max_length=300)

    def __str__(self):
        return self.nome_dieta

class RefeicaoBaseModel(models.Model):
    dieta = models.ForeignKey(Dieta, on_delete=models.CASCADE,)
    alimento = models.ForeignKey(Alimento, blank=True, on_delete=models.CASCADE,)
    quantidade = models.IntegerField(blank=True)

    class Meta:
        abstract=True

class SegDesjejum(models.Model):
    dieta = models.ForeignKey(Dieta, on_delete=models.CASCADE,)
    alimento = models.ForeignKey(Alimento, blank=True, on_delete=models.CASCADE,)
    quantidade = models.IntegerField(blank=True)

    class Meta:
        verbose_name = _("Desjejum")
        verbose_name_plural = _("Desjejuns")

    def __stf__(self):
        return self.alimento.nome

class SegAlmoco(RefeicaoBaseModel):
    class Meta:
        verbose_name = _("Almoço")
        verbose_name_plural = _("Almoços")

    def __stf__(self):
        return self.almento.nome

class SegJantar(RefeicaoBaseModel):
    class Meta:
        verbose_name = _("Almoço")
        verbose_name_plural = _("Almoços")

    def __stf__(self):
        return self.almento.nome

class SegLanches(RefeicaoBaseModel):
    class Meta:
        verbose_name = _("Almoço")
        verbose_name_plural = _("Almoços")

    def __stf__(self):
        return self.almento.nome

class TerDesjejum(RefeicaoBaseModel):
    class Meta:
        verbose_name = _("Almoço")
        verbose_name_plural = _("Almoços")

    def __stf__(self):
        return self.almento.nome

class TerAlmoco(RefeicaoBaseModel):
    class Meta:
        verbose_name = _("Almoço")
        verbose_name_plural = _("Almoços")

    def __stf__(self):
        return self.almento.nome

class TerJantar(RefeicaoBaseModel):
    class Meta:
        verbose_name = _("Almoço")
        verbose_name_plural = _("Almoços")

    def __stf__(self):
        return self.almento.nome

class TerLanches(RefeicaoBaseModel):
    class Meta:
        verbose_name = _("Almoço")
        verbose_name_plural = _("Almoços")

    def __stf__(self):
        return self.almento.nome

class QuaDesjejum(RefeicaoBaseModel):
    class Meta:
        verbose_name = _("Almoço")
        verbose_name_plural = _("Almoços")

    def __stf__(self):
        return self.almento.nome

class QuaAlmoco(RefeicaoBaseModel):
    class Meta:
        verbose_name = _("Almoço")
        verbose_name_plural = _("Almoços")

    def __stf__(self):
        return self.almento.nome

class QuaJantar(RefeicaoBaseModel):
    class Meta:
        verbose_name = _("Almoço")
        verbose_name_plural = _("Almoços")

    def __stf__(self):
        return self.almento.nome

class QuaLanches(RefeicaoBaseModel):
    class Meta:
        verbose_name = _("Almoço")
        verbose_name_plural = _("Almoços")

    def __stf__(self):
        return self.almento.nome

class QuiDesjejum(RefeicaoBaseModel):
    class Meta:
        verbose_name = _("Almoço")
        verbose_name_plural = _("Almoços")

    def __stf__(self):
        return self.almento.nome

class QuiAlmoco(RefeicaoBaseModel):
    class Meta:
        verbose_name = _("Almoço")
        verbose_name_plural = _("Almoços")

    def __stf__(self):
        return self.almento.nome

class QuiJantar(RefeicaoBaseModel):
    class Meta:
        verbose_name = _("Almoço")
        verbose_name_plural = _("Almoços")

    def __stf__(self):
        return self.almento.nome

class QuiLanches(RefeicaoBaseModel):
    class Meta:
        verbose_name = _("Almoço")
        verbose_name_plural = _("Almoços")

    def __stf__(self):
        return self.almento.nome

class SexDesjejum(RefeicaoBaseModel):
    class Meta:
        verbose_name = _("Almoço")
        verbose_name_plural = _("Almoços")

    def __stf__(self):
        return self.almento.nome

class SexAlmoco(RefeicaoBaseModel):
    class Meta:
        verbose_name = _("Almoço")
        verbose_name_plural = _("Almoços")

    def __stf__(self):
        return self.almento.nome

class SexJantar(RefeicaoBaseModel):
    class Meta:
        verbose_name = _("Almoço")
        verbose_name_plural = _("Almoços")

    def __stf__(self):
        return self.almento.nome

class SexLanches(RefeicaoBaseModel):
    class Meta:
        verbose_name = _("Almoço")
        verbose_name_plural = _("Almoços")

    def __stf__(self):
        return self.almento.nome

class SabDesjejum(RefeicaoBaseModel):
    class Meta:
        verbose_name = _("Almoço")
        verbose_name_plural = _("Almoços")

    def __stf__(self):
        return self.almento.nome

class SabAlmoco(RefeicaoBaseModel):
    class Meta:
        verbose_name = _("Almoço")
        verbose_name_plural = _("Almoços")

    def __stf__(self):
        return self.almento.nome

class SabJantar(RefeicaoBaseModel):
    class Meta:
        verbose_name = _("Almoço")
        verbose_name_plural = _("Almoços")

    def __stf__(self):
        return self.almento.nome

class SabLanches(RefeicaoBaseModel):
    class Meta:
        verbose_name = _("Almoço")
        verbose_name_plural = _("Almoços")

    def __stf__(self):
        return self.almento.nome

class DomDesjejum(RefeicaoBaseModel):
    class Meta:
        verbose_name = _("Almoço")
        verbose_name_plural = _("Almoços")

    def __stf__(self):
        return self.almento.nome

class DomAlmoco(RefeicaoBaseModel):
    class Meta:
        verbose_name = _("Almoço")
        verbose_name_plural = _("Almoços")

    def __stf__(self):
        return self.almento.nome

class DomJantar(RefeicaoBaseModel):
    class Meta:
        verbose_name = _("Almoço")
        verbose_name_plural = _("Almoços")

    def __stf__(self):
        return self.almento.nome

class DomLanches(RefeicaoBaseModel):
    class Meta:
        verbose_name = _("Almoço")
        verbose_name_plural = _("Almoços")

    def __stf__(self):
        return self.almento.nome
