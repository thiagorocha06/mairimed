from django.contrib import admin
from artigos.models import Artigo, Especialidade, Tema
from django.db import models

from pagedown.widgets import AdminPagedownWidget

class ArtigoModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget },
    }
    list_display = ["pk", "titulo", "data_de_criacao", "data_de_publicacao", "especialidade", "modulo"]
    list_filter = ["especialidade", "modulo"]
    search_fields = ["titulo"]
    class meta:
        model = Artigo

class EspecialidadeAdmin(admin.ModelAdmin):
    search_fields = ('especialidade', )


class TemaAdmin(admin.ModelAdmin):
    search_fields = ('tema', )
    list_display = ('tema', 'especialidade',)
    list_filter = ('especialidade',)

admin.site.register(Artigo, ArtigoModelAdmin)
admin.site.register(Especialidade, EspecialidadeAdmin)
admin.site.register(Tema, TemaAdmin)
