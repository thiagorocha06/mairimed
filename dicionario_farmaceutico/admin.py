from django.contrib import admin
from .models import Farmaco

class FarmacoModelAdmin(admin.ModelAdmin):
    list_display = ["nome", "classe", "subclasse"]
    list_filter = ["classe", "subclasse"]
    search_fields = ["nome"]
    class meta:
        model = Farmaco

admin.site.register(Farmaco, FarmacoModelAdmin)
