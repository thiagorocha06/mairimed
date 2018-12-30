from django.contrib import admin
from controles.models import Peso, Pressao, Glicemia, Temperatura

class PesoAdmin(admin.ModelAdmin):
    list_display = ["user", "peso",]

    class Meta:
        model = Peso

class PressaoAdmin(admin.ModelAdmin):
    list_display = ["user", "sistolica", 'diastolica']

    class Meta:
        model = Pressao

class GlicemiaAdmin(admin.ModelAdmin):
    list_display = ["user", "glicemia",]

    class Meta:
        model = Glicemia

class TemperaturaAdmin(admin.ModelAdmin):
    list_display = ["user", "temperatura",]

    class Meta:
        model = Temperatura

admin.site.register(Peso, PesoAdmin)
admin.site.register(Pressao, PressaoAdmin)
admin.site.register(Glicemia, GlicemiaAdmin)
admin.site.register(Temperatura, TemperaturaAdmin)
