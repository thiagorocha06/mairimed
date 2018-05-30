from django.contrib import admin
from portal_saude.models import Materia, Assunto, Patologia
from django.db import models

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
    list_display = ('assunto',)
    # list_filter = ('especialidade',)

class PatologiaAdmin(admin.ModelAdmin):
    search_fields = ('patologia', )
    list_display = ('patologia',)
    # list_filter = ('especialidade',)

admin.site.register(Materia, MateriaModelAdmin)
admin.site.register(Assunto, AssuntoAdmin)
admin.site.register(Patologia, PatologiaAdmin)
from django.contrib import admin

# Register your models here.
