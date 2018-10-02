from django.contrib import admin
from .models import PerfilEstudante

class PerfilEstudanteAdmin(admin.ModelAdmin):

    list_display = ["user", "email_confirmed"]
    search_fields = ["user",]

admin.site.register(PerfilEstudante, PerfilEstudanteAdmin)
