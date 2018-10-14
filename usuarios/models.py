import hashlib

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.conf import settings
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver

INSTITUICOES = ( ('1', '----'), ('2', 'ESCS'), ('3', 'UNB'), ('4', 'UCB'), ('5', 'UNICEUB'), ('6', 'FACIPLAC') )

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

class PerfilEstudante(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)
    primeiro_nome = models.CharField(max_length=30, default='')
    ultimo_nome = models.CharField(max_length=30, default='')
    faculdade = models.CharField(max_length=1, choices=INSTITUICOES, verbose_name = _("Instituição"), default="1")
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False)

    def gravatar_url(self):
        return "http://www.gravatar.com/avatar/%s?s=50" % hashlib.md5(self.user.email.encode('utf-8')).hexdigest()

    def get_absolute_url(self):
        return reverse('detail_user', kwargs={'pk': self.pk})

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        PerfilEstudante.objects.create(user=instance)
    instance.perfilestudante.save()
