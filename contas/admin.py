from django.contrib import admin
from .models import PerfilEstudante

class PerfilEstudanteAdmin(admin.ModelAdmin):

    list_display = ["estudante", "email_confirmed"]
    search_fields = ["estudante",]

admin.site.register(PerfilEstudante, PerfilEstudanteAdmin)
