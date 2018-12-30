from django.contrib import admin
from dieta.models import (
    Alimento, Dieta, SegDesjejum, SegAlmoco
)

class DesjejumInline(admin.TabularInline):
    model = SegDesjejum

class AlmocoInline(admin.TabularInline):
    model = SegAlmoco

class AlimentoAdmin(admin.ModelAdmin):
    list_display = ["nome", 'porcao', 'unidade']
    search_fields = ["nome",]

class DietaAdmin(admin.ModelAdmin):
    list_display = ['nome_dieta', 'user', 'pk']
    search_fields = ['nome_dieta']

    inlines = [DesjejumInline, AlmocoInline]

admin.site.register(Alimento, AlimentoAdmin)
admin.site.register(Dieta, DietaAdmin)
