from rest_framework import serializers
from .models import Facture, LigneFacture

class LigneFactureSerializer(serializers.ModelSerializer):
    total_ttc = serializers.ReadOnlyField()

    class Meta:
        model = LigneFacture
        fields = '__all__'

class FactureSerializer(serializers.ModelSerializer):
    lignes = LigneFactureSerializer(many=True, read_only=True)

    class Meta:
        model = Facture
        fields = '__all__'
