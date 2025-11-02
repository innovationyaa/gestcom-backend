from django.contrib import admin
from django import forms
from django.utils.html import format_html
from .models import Article, MouvementStock, Categorie, SousCategorie


# --- Formulaire personnalisé pour filtrer les sous-catégories dynamiquement ---
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'

    class Media:
        js = ('admin/js/article_admin.js',)  # si tu veux ajouter un JS


# --- Configuration de l’affichage de l’Article dans l’admin ---
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    form = ArticleForm
    list_display = (
        'reference',
        'categorie',
        'sous_categorie',
        'quantite_actuelle',
        'unite_mesure',  # corrigé ici
        'seuil_minimum',
        'prix_vente',
        'alerte_seuil',
    )
    search_fields = ('reference',)
    list_filter = ('categorie', 'sous_categorie', 'unite_mesure')

    def alerte_seuil(self, obj):
        if obj.quantite_actuelle < obj.seuil_minimum:
            return format_html('<span style="color: red; font-weight: bold;">⚠️ En rupture</span>')
        return format_html('<span style="color: green;">✔️ OK</span>')
    alerte_seuil.short_description = "Alerte Stock"


# --- Configuration du Mouvement de stock ---
@admin.register(MouvementStock)
class MouvementStockAdmin(admin.ModelAdmin):
    list_display = ('type_mouvement', 'article', 'quantite', 'date')
    list_filter = ('type_mouvement', 'date')
    search_fields = ('article__reference', 'article__sous_categorie__nom')


# --- Admin Categorie ---
@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ('nom',)


# --- Admin SousCategorie ---
@admin.register(SousCategorie)
class SousCategorieAdmin(admin.ModelAdmin):
    list_display = ('nom',)  # plus de catégorie
    search_fields = ('nom',)
