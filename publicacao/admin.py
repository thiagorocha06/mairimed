from django.contrib import admin
from publicacao.models import (
    Pergunta,
)

class PerguntaAdmin(admin.ModelAdmin):

    list_display = ["user", "content", "creation_date",]
    search_fields = ["user", "content"]
    list_filter = ('user',)

admin.site.register(Pergunta, PerguntaAdmin)
