from django.contrib import admin
from .models import Categorie, SousCategorie, Article, MouvementStock, UniteMesure


@admin.register(UniteMesure)
class UniteMesureAdmin(admin.ModelAdmin):
    list_display = ("nom",)
    search_fields = ("nom",)


@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ("nom",)
    search_fields = ("nom",)


@admin.register(SousCategorie)
class SousCategorieAdmin(admin.ModelAdmin):
    list_display = ("nom", "categorie")
    search_fields = ("nom", "categorie__nom")
    list_filter = ("categorie",)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        "reference",
        "description",
        "categorie",
        "sous_categorie",
        "unite_mesure",
        "quantite_actuelle",
        "prix_achat",
        "prix_vente",
        "fournisseur",
    )
    list_filter = ("categorie", "sous_categorie", "unite_mesure", "fournisseur")

    # ⚡ Ajout obligatoire pour corriger ton erreur
    search_fields = ["reference", "description"]


@admin.register(MouvementStock)
class MouvementStockAdmin(admin.ModelAdmin):
    list_display = ("article", "type_mouvement", "quantite", "date", "bon_livraison", "bon_commande")
    list_filter = ("type_mouvement", "date")
    search_fields = ("article__reference", "bon_livraison", "bon_commande")
