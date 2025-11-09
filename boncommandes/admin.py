from django.contrib import admin
from .models import BonCommande, DetailsBC

class DetailsBCInline(admin.TabularInline):
    model = DetailsBC
    extra = 1

@admin.register(BonCommande)
class BonCommandeAdmin(admin.ModelAdmin):
    list_display = ('numero_bc', 'fournisseur', 'date_commande', 'statut', 'montant_total')
    inlines = [DetailsBCInline]
