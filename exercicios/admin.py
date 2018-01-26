from django.contrib import admin
from exercicios.models import Exercicio

class ExercicioModelAdmin(admin.ModelAdmin):
    list_display = ["pk","enunciado", "especialidade", "ano", "localidade", "prova", "instituicao"]
    list_filter = ["especialidade", "ano", "localidade"]
    search_fields = ["enunciado"]
    class meta:
        model = Exercicio

admin.site.register(Exercicio, ExercicioModelAdmin)
