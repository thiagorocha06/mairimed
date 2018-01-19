from django.db import models
from django.utils import timezone

class Exercicio(models.Model):
    data_de_criacao = models.DateTimeField(default=timezone.now)
    especialidade = models.CharField(max_length=200, blank=True, null=True)
    tema = models.CharField(max_length=200, blank=True, null=True)
    prova = models.CharField(max_length=200, blank=True, null=True)
    instituicao = models.CharField(max_length=200, blank=True, null=True)
    ano = models.CharField(max_length=200, blank=True, null=True)
    enunciado = models.TextField(blank=True, null=True)
    exercicio_img1 = models.ImageField(upload_to='img', blank=True, null=True)
    exercicio_img2 = models.ImageField(upload_to='img', blank=True, null=True)
    alternativa1 = models.TextField(blank=True, null=True)
    alternativa2 = models.TextField(blank=True, null=True)
    alternativa3 = models.TextField(blank=True, null=True)
    alternativa4 = models.TextField(blank=True, null=True)
    alternativa5 = models.TextField(blank=True, null=True)
    resposta = models.TextField(blank=True, null=True)
    comentario = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.enunciado[:100]
