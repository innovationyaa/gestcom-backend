from rest_framework import serializers
from .models import Categorie, SousCategorie, Article, MouvementStock
from fournisseurs.models import Fournisseur
from fournisseurs.serializers import FournisseurSerializer


class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = ['id', 'nom']


class SousCategorieSerializer(serializers.ModelSerializer):
    # 🔥 Ajoute la catégorie associée (lecture seule)
    categorie = CategorieSerializer(read_only=True)
    # 🔥 Pour permettre la création ou modification via ID
    categorie_id = serializers.PrimaryKeyRelatedField(
        queryset=Categorie.objects.all(),
        source='categorie',
        write_only=True
    )

    class Meta:
        model = SousCategorie
        fields = ['id', 'nom', 'categorie', 'categorie_id']


class CategorieWithSousCategoriesSerializer(serializers.ModelSerializer):
    sous_categories = SousCategorieSerializer(many=True, read_only=True)

    class Meta:
        model = Categorie
        fields = ['id', 'nom', 'sous_categories']


class ArticleSerializer(serializers.ModelSerializer):
    fournisseur = FournisseurSerializer(read_only=True)
    fournisseur_id = serializers.PrimaryKeyRelatedField(
        queryset=Fournisseur.objects.all(),
        source='fournisseur',
        write_only=True
    )

    class Meta:
        model = Article
        fields = '__all__'


class MouvementStockSerializer(serializers.ModelSerializer):
    article_detail = ArticleSerializer(read_only=True, source='article')

    class Meta:
        model = MouvementStock
        fields = '__all__'
