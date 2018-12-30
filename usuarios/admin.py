from django.contrib import admin
from .models import PerfilUsuario, PerfilSaude, User, MinhaDieta, MeusSintomas

class PerfilUsuarioAdmin(admin.ModelAdmin):

    list_display = ["user", "email_confirmed"]
    search_fields = ["user",]

class PerfilSaudeAdmin(admin.ModelAdmin):

    list_display = ["user", "data_nascimento"]
    search_fields = ["user",]

class MinhaDietaAdmin(admin.ModelAdmin):

    list_display = ["user", "minha_dieta"]
    search_fields = ["user",]

class MeusSintomasAdmin(admin.ModelAdmin):

    list_display = ['user', 'meus_sintomas']
    search_fields = ['user']

class UserAdmin(admin.ModelAdmin):

    class Meta:
        model = User

admin.site.register(PerfilUsuario, PerfilUsuarioAdmin)
admin.site.register(PerfilSaude, PerfilSaudeAdmin)
admin.site.register(MinhaDieta, MinhaDietaAdmin)
admin.site.register(MeusSintomas, MeusSintomasAdmin)
admin.site.register(User, UserAdmin)
