from django.contrib import admin

from galeria.models import Fotografia

class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda", "descricao", "foto")
    list_display_links = ("id", "nome")
    list_filter = ("categoria",)
    search_fields = ("nome", "legenda")

admin.site.register(Fotografia, ListandoFotografias)
