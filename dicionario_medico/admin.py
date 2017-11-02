from django.contrib import admin
from .models import Termo

class TermoModelAdmin(admin.ModelAdmin):
    list_display = ["nome", "tipo"]
    list_filter = ["tipo"]
    search_fields = ["nome"]
    class meta:
        model = Termo

admin.site.register(Termo, TermoModelAdmin)
