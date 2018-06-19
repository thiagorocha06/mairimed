from django.contrib import admin
from .models import Farmaco

class FarmacoModelAdmin(admin.ModelAdmin):
    list_display = ["nome"]
    search_fields = ["nome"]
    class meta:
        model = Farmaco

admin.site.register(Farmaco, FarmacoModelAdmin)
