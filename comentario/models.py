from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.conf import settings
from django.db import models

class ComentManager(models.Manager):
    def filter_by_instance(self, instance):
        content_type = ContentType.objects.get_for_model(instance.__class__)
        obj_id = instance.pk
        qs = super(ComentManager, self).filter(content_type=content_type, object_id=obj_id)
        return qs

class Comentario(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    conteudo = models.TextField()
    data     = models.DateTimeField(auto_now_add=True)

    objects = ComentManager()

    def __str__(self):
        return str(self.user.username)
