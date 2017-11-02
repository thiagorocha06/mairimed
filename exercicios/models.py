from django.db import models

class Exercicio(models.Model):
    nome = models.CharField(max_length=50, blank=True, null=True)
    categoria = models.CharField(max_length=200, blank=True, null=True)
    exercicio_img = models.ImageField(upload_to='img', blank=True, null=True)
    exercicio_historia = models.TextField(blank=True, null=True)
    exercicio_resposta = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome
