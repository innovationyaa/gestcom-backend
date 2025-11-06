from django.contrib import admin
from .models import Fournisseur, FactureFournisseur, PaiementFournisseur


@admin.register(Fournisseur)
class FournisseurAdmin(admin.ModelAdmin):
    list_display = ('nom', 'contact', 'ice', 'if_fiscal')
    search_fields = ('nom', 'ice', 'if_fiscal')


@admin.register(FactureFournisseur)
class FactureFournisseurAdmin(admin.ModelAdmin):
    list_display = ('numero_facture', 'fournisseur', 'montant_total', 'statut', 'date_facture')
    list_filter = ('statut', 'fournisseur')
    search_fields = ('numero_facture',)


@admin.register(PaiementFournisseur)
class PaiementFournisseurAdmin(admin.ModelAdmin):
    list_display = ('facture', 'montant', 'date_paiement', 'mode_paiement')
    search_fields = ('facture__numero_facture',)
