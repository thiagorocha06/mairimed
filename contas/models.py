from django.db import models
from django.contrib.auth.models import User
import hashlib
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

INSTITUICOES = ( ('1', 'ESCS'), ('2', 'UNB'), ('3', 'UCB'), ('4', 'UNICEUB'), ('5', 'FACIPLAC') )

class PerfilEstudante(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)
    primeiro_nome = models.CharField(max_length=30, default='')
    ultimo_nome = models.CharField(max_length=30, default='')
    faculdade = models.CharField(max_length=1, choices=INSTITUICOES, verbose_name = _("Instituição"), default="1")
    matricula = models.CharField(max_length=50, default="")

    def gravatar_url(self):
        return "http://www.gravatar.com/avatar/%s?s=50" % hashlib.md5(self.user.email.encode('utf-8')).hexdigest()

    def get_absolute_url(self):
        return reverse('detail_user', kwargs={'pk': self.pk})

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        PerfilEstudante.objects.create(user=instance)
    instance.perfilestudante.save()
