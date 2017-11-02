from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from artigos.models import Artigo

class Estudante(models.Model):
    usuario = models.OneToOneField(User)
    primeiro_nome = models.CharField(max_length=50, default='')
    ultimo_nome = models.CharField(max_length=50, default='')
    instituicao = models.CharField(max_length=30, default='')
    semestre = models.CharField(max_length=10, default='')
    artigos_favoritos = models.ManyToManyField(Artigo, related_name='favorited_by')

def criar_estudante(sender, **kwargs):
    if kwargs['created']:
        estudante = Estudante.objects.create(nome=kwargs['instance'])

post_save.connect(criar_estudante, sender=User)
