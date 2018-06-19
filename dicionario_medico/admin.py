from django.contrib import admin
from .models import Termo, Doenca

class TermoModelAdmin(admin.ModelAdmin):
    list_display = ["nome", "tipo"]
    list_filter = ["tipo"]
    search_fields = ["nome"]
    class meta:
        model = Termo

class DoencaModelAdmin(admin.ModelAdmin):
    list_display = ["nome"]
    search_fields = ["nome"]
    class meta:
        model = Doenca

admin.site.register(Termo, TermoModelAdmin)
admin.site.register(Doenca, DoencaModelAdmin)
