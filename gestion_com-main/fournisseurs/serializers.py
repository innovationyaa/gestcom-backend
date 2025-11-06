from rest_framework import serializers
from .models import Fournisseur, FactureFournisseur, PaiementFournisseur


class FournisseurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fournisseur
        fields = '__all__'


class PaiementFournisseurSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaiementFournisseur
        fields = '__all__'


class FactureFournisseurSerializer(serializers.ModelSerializer):
    paiements = PaiementFournisseurSerializer(many=True, read_only=True)
    fournisseur_nom = serializers.CharField(source='fournisseur.nom', read_only=True)

    class Meta:
        model = FactureFournisseur
        fields = '__all__'
