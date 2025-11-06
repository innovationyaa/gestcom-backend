from django.contrib import admin
from .models import BonLivraison, DetailsBL

class DetailsBLInline(admin.TabularInline):
    model = DetailsBL
    extra = 1

@admin.register(BonLivraison)
class BonLivraisonAdmin(admin.ModelAdmin):
    list_display = ('numero_bl', 'bon_commande', 'date_livraison', 'statut')
    inlines = [DetailsBLInline]
