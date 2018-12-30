from django.db import models
from django.utils import timezone
from django.conf import settings

class Pressao(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    sistolica = models.IntegerField(null=True, blank=True)
    diastolica = models.IntegerField(null=True, blank=True)
    data = models.DateField(default=timezone.now)
    hora = models.TimeField(default=timezone.now)

    def __str__(self):
        return str(self.sistolica)

class Glicemia(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    glicemia = models.IntegerField(null=True, blank=True)
    data = models.DateField(default=timezone.now)
    hora = models.TimeField(default=timezone.now)

    def __str__(self):
        return str(self.glicemia)

class Temperatura(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    temperatura = models.IntegerField(null=True, blank=True)
    data = models.DateField(default=timezone.now)
    hora = models.TimeField(default=timezone.now)

    def __str__(self):
        return str(self.tempetura)

class Peso(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    peso = models.IntegerField(null=True, blank=True)
    data = models.DateField(default=timezone.now)
    hora = models.TimeField(default=timezone.now)

    def __str__(self):
        return str(self.peso)
