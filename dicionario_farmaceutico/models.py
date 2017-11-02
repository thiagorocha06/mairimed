from django.db import models

class Farmaco(models.Model):
    nome = models.TextField(max_length=50, blank=True, null=True)
    classe = models.TextField(blank=True, null=True)
    subclasse = models.TextField(blank=True, null=True)
    marcas = models.TextField(blank=True, null=True)
    farmacodinamica = models.TextField(blank=True, null=True)
    farmacocinetica = models.TextField(blank=True, null=True)
    absorcao = models.TextField(blank=True, null=True)
    distribuicao = models.TextField(blank=True, null=True)
    metabolismo = models.TextField(blank=True, null=True)
    eliminacao = models.TextField(blank=True, null=True)
    indicacoes = models.TextField(blank=True, null=True)
    posologia = models.TextField(blank=True, null=True)
    pediatria = models.TextField(blank=True, null=True)
    administracao = models.TextField(blank=True, null=True)
    rmuitocomum = models.TextField(blank=True, null=True)
    rcomum = models.TextField(blank=True, null=True)
    rincomum = models.TextField(blank=True, null=True)
    rrara = models.TextField(blank=True, null=True)
    rmuitorara = models.TextField(blank=True, null=True)
    rnaodefinida = models.TextField(blank=True, null=True)
    alteracaoexames = models.TextField(blank=True, null=True)
    contraindicacoes = models.TextField(blank=True, null=True)
    gravidez = models.TextField(blank=True, null=True)
    lactacao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome
