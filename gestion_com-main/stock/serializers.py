from rest_framework import serializers
from .models import Article, MouvementStock, Categorie, SousCategorie
from fournisseurs.models import Fournisseur
from fournisseurs.serializers import FournisseurSerializer


# ---- Catégories ----
class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = '__all__'


# ---- Sous-catégories ----
class SousCategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = SousCategorie
        fields = '__all__'


# ---- Articles ----
class ArticleSerializer(serializers.ModelSerializer):
    fournisseur = FournisseurSerializer(read_only=True)
    fournisseur_id = serializers.PrimaryKeyRelatedField(
        queryset=Fournisseur.objects.all(),
        source='fournisseur',
        write_only=True
    )

    categorie = CategorieSerializer(read_only=True)
    categorie_id = serializers.PrimaryKeyRelatedField(
        queryset=Categorie.objects.all(),
        source='categorie',
        write_only=True
    )

    sous_categorie = SousCategorieSerializer(read_only=True)
    sous_categorie_id = serializers.PrimaryKeyRelatedField(
        queryset=SousCategorie.objects.all(),
        source='sous_categorie',
        write_only=True
    )

    class Meta:
        model = Article
        fields = '__all__'


# ---- Mouvements de stock ----
class MouvementStockSerializer(serializers.ModelSerializer):
    article_detail = ArticleSerializer(read_only=True, source='article')

    class Meta:
        model = MouvementStock
        fields = '__all__'
