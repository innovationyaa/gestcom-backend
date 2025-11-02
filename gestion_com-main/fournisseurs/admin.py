from django.contrib import admin
from .models import Fournisseur

@admin.register(Fournisseur)
class FournisseurAdmin(admin.ModelAdmin):
    list_display = ('nom', 'ice', 'if_fiscal', 'contact', 'adresse')
    search_fields = ('nom', 'ice', 'if_fiscal')
