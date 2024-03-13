from django.contrib import admin

from apps.galeria.models import Fotografia

class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda", "descricao", "foto", "publicada")
    list_display_links = ("id", "nome")
    list_filter = ("categoria", "usuario")
    search_fields = ("nome", "legenda")
    list_editable = ("publicada",)
    #list_per_page = 10
    #ordering = ("nome",)

admin.site.register(Fotografia, ListandoFotografias)
