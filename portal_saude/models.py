from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation
from hitcount.models import HitCount, HitCountMixin
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext as _
from model_utils.managers import InheritanceManager

@python_2_unicode_compatible
class Assunto(models.Model):

    assunto = models.CharField(
        verbose_name=_("Assunto"),
        max_length=250, blank=True, null=True)

    class Meta:
        verbose_name = _("Assunto")
        verbose_name_plural = _("Assuntos")

    def __str__(self):
        return self.assunto

@python_2_unicode_compatible
class Patologia(models.Model):

    patologia = models.CharField(
        verbose_name=_("Patologia"),
        max_length=250, blank=True, null=True)

    class Meta:
        verbose_name = _("Patologia")
        verbose_name_plural = _("Patologias")

    def __str__(self):
        return self.patologia

class Materia(models.Model, HitCountMixin):
    author = models.ForeignKey('auth.User')
    hit_count_generic = GenericRelation(
        HitCount, object_id_field='object_pk',
        related_query_name='hit_count_generic_relation')
    data_de_criacao = models.DateTimeField(default=timezone.now)
    data_de_publicacao = models.DateTimeField(blank=True, null=True)

    destaque_geral1 = models.BooleanField(
        blank=True, default=False,
        verbose_name=_("Materia destaque geral 1"),
        help_text=_("Se marcado, a materia sera mostrado na página destaque geral como número 1"))

    destaque_geral2 = models.BooleanField(
        blank=True, default=False,
        verbose_name=_("Materia destaque geral 2"),
        help_text=_("Se marcado, a materia sera mostrado na página destaque geral como número 2"))

    destaque_geral3 = models.BooleanField(
        blank=True, default=False,
        verbose_name=_("Materia destaque geral 3"),
        help_text=_("Se marcado, a materia sera mostrado na página destaque geral como número 3"))

    destaque_patologia = models.BooleanField(
        blank=True, default=False,
        verbose_name=_("Materia destaque da patologia"),
        help_text=_("Se marcado, o materia sera mostrado na página destaque da patologia. Marcar 3 por patologia"))

    patologia = models.ForeignKey(
        Patologia, null=True, blank=True,
        verbose_name=_("Patologia"))

    assunto = models.ForeignKey(
        Assunto, null=True, blank=True,
        verbose_name=_("Assunto"))

    titulo = models.CharField(max_length=200)

    figura_maior = models.ImageField(upload_to='img/portal_saude', blank=True, null=True,
                            help_text=_("Corresponde à figura de destaque geral"))
    titulo_figura_texto = models.CharField(max_length=200, blank=True, null=True,
                            help_text=_("Corresponde ao texto de destaque geral"))

    url = models.SlugField(
        max_length=60, blank=False, null=True,
        help_text=_("a user friendly url"),
        verbose_name=_("user friendly url"))

    top1 = models.CharField(max_length=200, blank=True, null=True,)
    texto1 = models.TextField(blank=True, null=True)
    figura1 = models.ImageField(upload_to='img/portal_saude', blank=True, null=True)
    figura1_texto = models.CharField(max_length=200, blank=True, null=True)

    def publicar(self):
        self.data_de_publicacao = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo
