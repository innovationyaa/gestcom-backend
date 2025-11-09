# bonlivraisons/serializers.py
from rest_framework import serializers
from .models import BonLivraison, DetailsBL


class DetailsBLSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailsBL
        fields = ['id', 'article', 'quantite']


class BonLivraisonSerializer(serializers.ModelSerializer):
    details = DetailsBLSerializer(many=True)

    class Meta:
        model = BonLivraison
        fields = ['id', 'numero_bl', 'bon_commande', 'date_livraison', 'statut', 'details']

    def create(self, validated_data):
        details_data = validated_data.pop('details', [])
        bl = BonLivraison.objects.create(**validated_data)
        for detail in details_data:
            DetailsBL.objects.create(bon_livraison=bl, **detail)
        # 🔥 Crée les mouvements automatiquement
        bl.creer_mouvements_stock()
        return bl
