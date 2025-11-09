from django.contrib import admin
from .models import BonLivraison, DetailsBL


class DetailsBLInline(admin.TabularInline):
    model = DetailsBL
    extra = 1
    autocomplete_fields = ['article']  # ✅ fonctionne grâce à search_fields dans ArticleAdmin


@admin.register(BonLivraison)
class BonLivraisonAdmin(admin.ModelAdmin):
    list_display = ("numero_bl", "get_fournisseur", "date_livraison", "statut")
    search_fields = ("numero_bl", "bon_commande__fournisseur__nom")
    list_filter = ("statut", "date_livraison")
    inlines = [DetailsBLInline]

    # ✅ méthode pour afficher le fournisseur relié via BonCommande
    def get_fournisseur(self, obj):
        return obj.bon_commande.fournisseur.nom if obj.bon_commande and obj.bon_commande.fournisseur else "—"
    get_fournisseur.short_description = "Fournisseur"
