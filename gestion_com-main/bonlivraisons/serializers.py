from rest_framework import serializers
from .models import BonLivraison, DetailsBL
from stock.serializers import ArticleSerializer
from boncommandes.serializers import BonCommandeSerializer


class DetailsBLSerializer(serializers.ModelSerializer):
    article_detail = ArticleSerializer(source='article', read_only=True)

    class Meta:
        model = DetailsBL
        fields = ['id', 'article', 'article_detail', 'quantite']


class BonLivraisonSerializer(serializers.ModelSerializer):
    bon_commande_detail = BonCommandeSerializer(source='bon_commande', read_only=True)
    details = DetailsBLSerializer(many=True)

    class Meta:
        model = BonLivraison
        fields = ['id', 'numero_bl', 'bon_commande', 'bon_commande_detail', 'date_livraison', 'statut', 'details']

    def create(self, validated_data):
        details_data = validated_data.pop('details')
        bon_livraison = BonLivraison.objects.create(**validated_data)
        for d in details_data:
            DetailsBL.objects.create(bon_livraison=bon_livraison, **d)
        bon_livraison.verifier_statut()
        return bon_livraison
