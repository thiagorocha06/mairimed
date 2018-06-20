from django.contrib import admin
from portal_saude.models import Materia, Assunto, Patologia
from django.db import models
from dicionario_farmacos.models import Farmaco
from dicionario_doencas.models import Doenca
from dicionario_alimentos.models import Alimento
from dicionario_termos.models import Termo
from pagedown.widgets import AdminPagedownWidget

class MateriaModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget },
    }
    list_display = ["titulo", "data_de_publicacao", "assunto", "patologia"]
    list_filter = ["assunto", "patologia"]
    search_fields = ["titulo", 'assunto']
    class meta:
        model = Materia

class AssuntoAdmin(admin.ModelAdmin):
    search_fields = ('assunto', )
    list_display = ('assunto', 'pk')
    # list_filter = ('especialidade',)

class PatologiaAdmin(admin.ModelAdmin):
    search_fields = ('patologia', )
    list_display = ('patologia', )
    # list_filter = ('especialidade',)

class AlimentoModelAdmin(admin.ModelAdmin):
    list_display = ["nome", "tipo"]
    search_fields = ["nome"]
    class meta:
        model = Alimento

class DoencaModelAdmin(admin.ModelAdmin):
    list_display = ["nome"]
    search_fields = ["nome"]
    class meta:
        model = Doenca

class FarmacoModelAdmin(admin.ModelAdmin):
    list_display = ["nome"]
    search_fields = ["nome"]
    class meta:
        model = Farmaco

class TermoModelAdmin(admin.ModelAdmin):
    list_display = ["nome", "tipo"]
    list_filter = ["tipo"]
    search_fields = ["nome"]
    class meta:
        model = Termo

admin.site.register(Alimento, AlimentoModelAdmin)
admin.site.register(Doenca, DoencaModelAdmin)
admin.site.register(Farmaco, FarmacoModelAdmin)
admin.site.register(Termo, TermoModelAdmin)

admin.site.register(Materia, MateriaModelAdmin)
admin.site.register(Assunto, AssuntoAdmin)
admin.site.register(Patologia, PatologiaAdmin)
