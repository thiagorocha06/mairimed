import hashlib
import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.conf import settings
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from dieta.models import Dieta
from medicamento.models import Medicamento
from sintoma.models import Sintoma
from recomendacao.models import Recomendacao

INSTITUICOES = ( ('1', '----'), ('2', 'ESCS'), ('3', 'UNB'), ('4', 'UCB'), ('5', 'UNICEUB'), ('6', 'FACIPLAC') )
SEXO = ( ('1', 'Masculino'), ('2', 'Feminino') )

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)

class PerfilUsuario(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)
    primeiro_nome = models.CharField(max_length=30, default='')
    ultimo_nome = models.CharField(max_length=30, default='')
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False, blank=True)

    def gravatar_url(self):
        return "http://www.gravatar.com/avatar/%s?s=50" % hashlib.md5(self.user.email.encode('utf-8')).hexdigest()

    def get_absolute_url(self):
        return reverse('perfil')

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        PerfilUsuario.objects.create(user=instance)
        PerfilSaude.objects.create(user=instance)
    instance.perfilusuario.save()
    instance.perfilsaude.save()

class PerfilSaude(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    data_nascimento = models.DateField(null=True, blank=True, default=timezone.now)
    sexo = models.CharField(null=True, blank=True, max_length=1, choices=SEXO, verbose_name = _("Sexo"))
    altura = models.DecimalField(null=True, blank=True, max_digits=3, decimal_places=2)
    peso = models.IntegerField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('inicio')

    def idade(self):
        ano_nascimento = self.data_nascimento.year
        ano_atual = datetime.datetime.now().year
        idade = ano_atual - ano_nascimento
        return idade

class MinhaDieta(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    minha_dieta = models.ForeignKey(Dieta, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.minha_dieta.nome_dieta

class MeusSintomas(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    meus_sintomas = models.ForeignKey(Sintoma, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.meus_sintomas.sintoma

class MinhasRecomendacoes(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    minhas_recomendacoes = models.ManyToManyField(Recomendacao, blank=True)

class MeusMedicamentos(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    meus_medicamentos = models.ManyToManyField(Medicamento, blank=True)
