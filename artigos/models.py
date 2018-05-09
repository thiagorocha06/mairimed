# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation
from hitcount.models import HitCount, HitCountMixin
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext as _
from model_utils.managers import InheritanceManager

class EspecialidadeManager(models.Manager):

    def nova_especialidade(self, especialidade):
        nova_especialidade = self.create(especialidade=re.sub('\s+', '-', especialidade)
                                   .lower())

        nova_especialidade.save()
        return nova_especialidade

@python_2_unicode_compatible
class Especialidade(models.Model):

    especialidade = models.CharField(
        verbose_name=_("Especialidade"),
        max_length=250, blank=True,
        unique=True, null=True)

    objects = EspecialidadeManager()

    class Meta:
        verbose_name = _("Especialidade")
        verbose_name_plural = _("Especialidades")

    def __str__(self):
        return self.especialidade

@python_2_unicode_compatible
class Tema(models.Model):

    tema = models.CharField(
        verbose_name=_("Tema"),
        max_length=250, blank=True, null=True)

    ordem = models.CharField(
        verbose_name=_("Ordem"),
        max_length=250, blank=False, null=True)

    especialidade = models.ForeignKey(
        Especialidade, null=True, blank=True,
        verbose_name=_("Especialidade"))

    exercicios = models.ForeignKey(
        'quiz.Quiz', null=True, blank=True,
        verbose_name=_("Exercícios"))

    objects = EspecialidadeManager()

    class Meta:
        verbose_name = _("Tema")
        verbose_name_plural = _("Temas")

    def __str__(self):
        return self.tema

@python_2_unicode_compatible
class TemaBasico(models.Model):

    tema_basico = models.CharField(
        verbose_name=_("Tema Básico"),
        max_length=250, blank=True,
        unique=True, null=True)

    objects = EspecialidadeManager()

    class Meta:
        verbose_name = _("Tema Básico")
        verbose_name_plural = _("Temas Básicos")

    def __str__(self):
        return self.tema_basico

class Artigo(models.Model, HitCountMixin):
    author = models.ForeignKey('auth.User')
    hit_count_generic = GenericRelation(
        HitCount, object_id_field='object_pk',
        related_query_name='hit_count_generic_relation')
    data_de_criacao = models.DateTimeField(default=timezone.now)
    data_de_publicacao = models.DateTimeField(blank=True, null=True)

    artigo_interno = models.BooleanField(
        blank=True, default=False,
        verbose_name=_("Artigo para Internos"),
        help_text=_("Se marcado, o artigo sera mostrado apenas para internos conectados"))

    destaque_geral = models.BooleanField(
        blank=True, default=False,
        verbose_name=_("Artigo destaque geral"),
        help_text=_("Se marcado, o artigo sera mostrado na página destaque geral"))

    destaque_semana = models.BooleanField(
        blank=True, default=False,
        verbose_name=_("Artigo destaque da semana"),
        help_text=_("Se marcado, o artigo sera mostrado na página destaque da semana"))

    especialidade = models.ForeignKey(
        Especialidade, null=True, blank=True,
        verbose_name=_("Especialidade"))

    tema = models.ForeignKey(
        Tema, null=True, blank=True,
        verbose_name=_("Tema"))

    tema_basico = models.ForeignKey(
        TemaBasico, null=True, blank=True,
        verbose_name=_("Tema Basico"))

    modulo = models.CharField(max_length=200, blank=True, null=True)
    titulo = models.CharField(max_length=200)

    url = models.SlugField(
        max_length=60, blank=False, null=True,
        help_text=_("a user friendly url"),
        verbose_name=_("user friendly url"))

    apresentacao = models.CharField(max_length=200, blank=True, null=True)

    intro_top = models.CharField(max_length=200, blank=True, null=True,)
    introducao = models.TextField(blank=True, null=True)
    intro_figura1 = models.ImageField(upload_to='img', blank=True, null=True)
    intro_figura1_texto = models.CharField(max_length=200, blank=True, null=True)
    intro_figura2 = models.ImageField(upload_to='img', blank=True, null=True)
    intro_figura2_texto = models.CharField(max_length=200, blank=True, null=True)

    epidemio_top = models.CharField(max_length=200, blank=True, null=True,)
    epidemiologia = models.TextField(blank=True, null=True)
    epidemio_figura = models.ImageField(upload_to='img', blank=True, null=True)
    epidemio_figura_texto = models.CharField(max_length=200, blank=True, null=True)

    class_top = models.CharField(max_length=200, blank=True, null=True,)
    classificacao = models.TextField(blank=True, null=True)
    clas_figura = models.ImageField(upload_to='img', blank=True, null=True)
    clas_figura_texto = models.CharField(max_length=200, blank=True, null=True)

    etio_top = models.CharField(max_length=200, blank=True, null=True,)
    etiologia_fisiopatologia = models.TextField(blank=True, null=True)
    etio_img1 = models.ImageField(upload_to='img', blank=True, null=True)
    etio_img1_texto = models.CharField(max_length=200, blank=True, null=True)
    etio_img2 = models.ImageField(upload_to='img', blank=True, null=True)
    etio_img2_texto = models.CharField(max_length=200, blank=True, null=True)

    diag_top = models.CharField(max_length=200, blank=True, null=True,)
    diagnostico = models.TextField(blank=True, null=True)

    historia_figura = models.ImageField(upload_to='img', blank=True, null=True)
    historia_figura_texto = models.CharField(max_length=200, blank=True, null=True)

    ef_figura = models.ImageField(upload_to='img', blank=True, null=True)
    ef_figura_texto = models.CharField(max_length=200, blank=True, null=True)

    exames_top_h2 = models.CharField(max_length=200, blank=True, null=True)
    exames_complementares = models.TextField(blank=True, null=True)
    exames_img1 = models.ImageField(upload_to='img', blank=True, null=True)
    exames_img1_texto = models.CharField(max_length=200, blank=True, null=True)
    exames_img2 = models.ImageField(upload_to='img', blank=True, null=True)
    exames_img2_texto = models.CharField(max_length=200, blank=True, null=True)
    exames_img3 = models.ImageField(upload_to='img', blank=True, null=True)
    exames_img3_texto = models.CharField(max_length=200, blank=True, null=True)

    criterios_top = models.CharField(max_length=200, blank=True, null=True,)
    criterios_diagnosticos = models.TextField(blank=True, null=True)

    dd_top_h2 = models.CharField(max_length=200, blank=True, null=True)
    diagnostico_diferencial = models.TextField(blank=True, null=True)
    dd_img = models.ImageField(upload_to='img', blank=True, null=True)
    dd_img_texto = models.CharField(max_length=200, blank=True, null=True)

    diag_figura = models.ImageField(upload_to='img', blank=True, null=True)
    diag_figura_texto = models.CharField(max_length=200, blank=True, null=True)

    top1 = models.CharField(max_length=200, blank=True, null=True)
    texto1 = models.TextField(blank=True, null=True)
    top1_img1 = models.ImageField(upload_to='img', blank=True, null=True)
    top1_img1_texto = models.CharField(max_length=200, blank=True, null=True)
    top1_img2 = models.ImageField(upload_to='img', blank=True, null=True)
    top1_img2_texto = models.CharField(max_length=200, blank=True, null=True)

    tratamento_top = models.CharField(max_length=200, blank=True, null=True,)
    tratamento_e_manejo = models.TextField(blank=True, null=True)

    trat_figura = models.ImageField(upload_to='img', blank=True, null=True)
    trat_figura_texto = models.CharField(max_length=200, blank=True, null=True)

    profilaxia_top = models.CharField(max_length=200, blank=True, null=True,)
    profilaxia = models.TextField(blank=True, null=True)
    prof_figura = models.ImageField(upload_to='img', blank=True, null=True)
    prof_figura_texto = models.CharField(max_length=200, blank=True, null=True)

    prognostico_top = models.CharField(max_length=200, blank=True, null=True,)
    prognostico = models.TextField(blank=True, null=True)
    prognostico_img = models.ImageField(upload_to='img', blank=True, null=True)
    prognostico_img_texto = models.CharField(max_length=200, blank=True, null=True)

    complicacoes_top = models.CharField(max_length=200, blank=True, null=True,)
    complicacoes = models.TextField(blank=True, null=True)

    algoritmo_top = models.CharField(max_length=200, blank=True, null=True, default="ALGORITMO")
    algoritmo_img1 = models.ImageField(upload_to='img', blank=True, null=True)
    algoritmo_img1_texto = models.CharField(max_length=200, blank=True, null=True)
    algoritmo_img2 = models.ImageField(upload_to='img', blank=True, null=True)
    algoritmo_img2_texto = models.CharField(max_length=200, blank=True, null=True)
    algoritmo_img3 = models.ImageField(upload_to='img', blank=True, null=True)
    algoritmo_img3_texto = models.CharField(max_length=200, blank=True, null=True)
    referencias_top = models.CharField(max_length=200, blank=True, null=True, default="REFERÊNCIAS")
    referencias = models.TextField(blank=True, null=True)

    def publicar(self):
        self.data_de_publicacao = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo
