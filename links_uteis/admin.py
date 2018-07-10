from django.contrib import admin
from links_uteis.models import Link, Instituicao
from django.db import models

class LinkModelAdmin(admin.ModelAdmin):
    list_display = ["nome", "instituicao", 'link']
    list_filter = ["instituicao",]
    search_fields = ["nome"]
    class meta:
        model = Link

class InstituicaoModelAdmin(admin.ModelAdmin):
    search_fields = ('instituicao', )

admin.site.register(Instituicao, InstituicaoModelAdmin)
admin.site.register(Link, LinkModelAdmin)
