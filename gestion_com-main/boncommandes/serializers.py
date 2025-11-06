from rest_framework import serializers
from .models import BonCommande, DetailsBC
from stock.serializers import ArticleSerializer
from fournisseurs.serializers import FournisseurSerializer


class DetailsBCSerializer(serializers.ModelSerializer):
    article_detail = ArticleSerializer(source='article', read_only=True)

    class Meta:
        model = DetailsBC
        fields = ['id', 'article', 'article_detail', 'quantite', 'prix_unitaire', 'prix_total']


class BonCommandeSerializer(serializers.ModelSerializer):
    fournisseur_detail = FournisseurSerializer(source='fournisseur', read_only=True)
    details = DetailsBCSerializer(many=True)

    class Meta:
        model = BonCommande
        fields = ['id', 'numero_bc', 'fournisseur', 'fournisseur_detail', 'date_commande', 'statut', 'montant_total', 'notes', 'details']

    def create(self, validated_data):
        details_data = validated_data.pop('details')
        bon_commande = BonCommande.objects.create(**validated_data)
        for d in details_data:
            DetailsBC.objects.create(bon_commande=bon_commande, **d)
        bon_commande.calculer_total()
        return bon_commande
