from django.contrib import admin
from .models import Facture, LigneFacture

@admin.register(Facture)
class FactureAdmin(admin.ModelAdmin):
    list_display = ('numero', 'client', 'date_emission', 'montant_ttc', 'statut')
    search_fields = ('numero', 'client__nom')
    list_filter = ('statut', 'date_emission')

@admin.register(LigneFacture)
class LigneFactureAdmin(admin.ModelAdmin):
    list_display = ('facture', 'article', 'quantite', 'prix_unitaire', 'tva')
