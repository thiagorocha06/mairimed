from django.contrib import admin

from comentario.models import (
    Comentario,
)


class ComentarioAdmin(admin.ModelAdmin):

    list_display = ['pk', "user", "data"]
    search_fields = ["user", ]

admin.site.register(Comentario, ComentarioAdmin)
