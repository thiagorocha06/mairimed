from django.contrib import admin
from exercicios.models import Exercicio

class ExercicioModelAdmin(admin.ModelAdmin):
    list_display = ["pk","enunciado", "especialidade","tema", "ano", "localidade"]
    list_filter = ["localidade", "especialidade", "tema"]
    search_fields = ["enunciado"]
    class meta:
        model = Exercicio

admin.site.register(Exercicio, ExercicioModelAdmin)
