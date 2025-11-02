from rest_framework import serializers
from .models import Article, MouvementStock
from fournisseurs.models import Fournisseur
from fournisseurs.serializers import FournisseurSerializer  # ✅ import

class ArticleSerializer(serializers.ModelSerializer):
    # Afficher les infos du fournisseur
    fournisseur = FournisseurSerializer(read_only=True)
    # Permettre de créer/modifier via ID du fournisseur
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
