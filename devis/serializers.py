from rest_framework import serializers
from .models import Devis, LigneDevis
from clients.models import Client
from stock.models import Article


class LigneDevisSerializer(serializers.ModelSerializer):
    article_nom = serializers.CharField(source='article.nom', read_only=True)

    class Meta:
        model = LigneDevis
        fields = ['id', 'article', 'article_nom', 'quantite', 'prix_unitaire', 'tva']


class DevisSerializer(serializers.ModelSerializer):
    lignes = LigneDevisSerializer(many=True)
    client_nom = serializers.CharField(source='client.nom', read_only=True)

    class Meta:
        model = Devis
        fields = [
            'id', 'numero', 'date', 'client', 'client_nom', 'statut',
            'remise', 'taxe', 'total_ht', 'total_ttc', 'lignes'
        ]

    def create(self, validated_data):
        lignes_data = validated_data.pop('lignes')
        devis = Devis.objects.create(**validated_data)
        for ligne_data in lignes_data:
            LigneDevis.objects.create(devis=devis, **ligne_data)
        return devis

    def update(self, instance, validated_data):
        lignes_data = validated_data.pop('lignes', [])
        instance.statut = validated_data.get('statut', instance.statut)
        instance.remise = validated_data.get('remise', instance.remise)
        instance.taxe = validated_data.get('taxe', instance.taxe)
        instance.save()

        instance.lignes.all().delete()
        for ligne_data in lignes_data:
            LigneDevis.objects.create(devis=instance, **ligne_data)
        return instance
