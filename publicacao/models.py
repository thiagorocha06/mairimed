from django.db import models
from django.conf import settings
from comentario.models import Comentario

class Pergunta(models.Model):
    content = models.CharField(max_length=140)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now=True, blank=True)

    @property
    def comentarios(self):
        instance = self
        qs = Comentario.objects.filter_by_instance(self)
        return qs

    @property
    def get_content_type(self):
        instance = self
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return content_type
