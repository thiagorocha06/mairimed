from django.contrib import admin
from artigos.models import Artigo, Especialidade, Tema, TemaBasico
from django.db import models

from pagedown.widgets import AdminPagedownWidget

class ArtigoModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget },
    }
    list_display = ["titulo", "data_de_publicacao", "especialidade", "tema", "tema_basico"]
    list_filter = ["especialidade", "tema"]
    search_fields = ["titulo"]
    class meta:
        model = Artigo

class EspecialidadeAdmin(admin.ModelAdmin):
    search_fields = ('especialidade', )

class TemaAdmin(admin.ModelAdmin):
    search_fields = ('tema', )
    list_display = ('tema', 'especialidade',)
    list_filter = ('especialidade',)

class TemaBasicoAdmin(admin.ModelAdmin):
    search_fields = ('tema_basico', )

admin.site.register(Artigo, ArtigoModelAdmin)
admin.site.register(Especialidade, EspecialidadeAdmin)
admin.site.register(Tema, TemaAdmin)
admin.site.register(TemaBasico, TemaBasicoAdmin)
