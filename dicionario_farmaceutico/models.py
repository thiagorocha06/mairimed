from django.db import models

class Farmaco(models.Model):
    nome = models.CharField(max_length=50, blank=True, null=True)
    introducao = models.TextField(blank=True, null=True)
    indicacoes = models.TextField(blank=True, null=True)
    farmacodinamica = models.TextField(blank=True, null=True)
    farmacocinetica = models.TextField(blank=True, null=True)
    contraindicacoes = models.TextField(blank=True, null=True)
    precaucoes = models.TextField(blank=True, null=True)
    gravidez = models.TextField(blank=True, null=True)
    interacoes = models.TextField(blank=True, null=True)
    posologia = models.TextField(blank=True, null=True)
    reacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome
