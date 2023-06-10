from django.contrib import admin
from apps.galeria.models import Fotografia


class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda", "publicado", "quantidade_visitas")
    list_display_links = ("id", "nome")
    search_fields = ("nome",) # Este parâmetro deve ser uma tupla, por isso foi adicionada vírgula
    list_filter = ("categoria","usuario",)
    list_editable = ("publicado",)
    list_per_page = 10

admin.site.register(Fotografia, ListandoFotografias)