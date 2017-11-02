from django.db import models

class Termo(models.Model):
    nome = models.TextField(max_length=50, blank=True, null=True)
    tipo = models.TextField(max_length=50, blank=True, null=True)
    origem = models.TextField(max_length=50, blank=True, null=True)
    definicao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome
