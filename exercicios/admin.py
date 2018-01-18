from django.contrib import admin
from exercicios.models import Exercicio

class ExercicioModelAdmin(admin.ModelAdmin):
    list_display = ["especialidade", "ano", "prova", "instituicao", "enunciado"]
    list_filter = ["especialidade", "ano"]
    search_fields = ["enunciado"]
    class meta:
        model = Exercicio

admin.site.register(Exercicio, ExercicioModelAdmin)
