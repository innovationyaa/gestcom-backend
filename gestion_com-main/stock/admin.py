from django.contrib import admin
from django import forms
from .models import Categorie, SousCategorie, Article, MouvementStock


# ---------- FORMULAIRE PERSONNALISÉ ----------
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'

    class Media:
        # Ce fichier JS permet de filtrer les sous-catégories selon la catégorie choisie
        js = ('admin/js/article_admin.js',)


# ---------- ADMIN CATEGORIE ----------
@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ('nom',)


# ---------- ADMIN SOUS-CATEGORIE ----------
@admin.register(SousCategorie)
class SousCategorieAdmin(admin.ModelAdmin):
    list_display = ('nom', 'categorie')
    list_filter = ('categorie',)
    search_fields = ('nom', 'categorie__nom')


# ---------- ADMIN ARTICLE ----------
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    form = ArticleForm
    list_display = (
        'reference',
        'categorie',
        'sous_categorie',
        'quantite_actuelle',
        'prix_vente',
        'fournisseur',
    )
    list_filter = ('categorie', 'sous_categorie', 'fournisseur')
    search_fields = ('reference', 'description')
    autocomplete_fields = ('categorie', 'sous_categorie', 'fournisseur')


# ---------- ADMIN MOUVEMENT STOCK ----------
@admin.register(MouvementStock)
class MouvementStockAdmin(admin.ModelAdmin):
    list_display = ('type_mouvement', 'article', 'quantite', 'date')
    list_filter = ('type_mouvement', 'date')
    search_fields = ('article__reference',)
