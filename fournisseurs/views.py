from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Fournisseur, FactureFournisseur, PaiementFournisseur
from .serializers import FournisseurSerializer, FactureFournisseurSerializer, PaiementFournisseurSerializer


class FournisseurViewSet(viewsets.ModelViewSet):
    queryset = Fournisseur.objects.all().order_by('-date_creation')
    serializer_class = FournisseurSerializer


class FactureFournisseurViewSet(viewsets.ModelViewSet):
    queryset = FactureFournisseur.objects.all().order_by('-date_creation')
    serializer_class = FactureFournisseurSerializer

    @action(detail=True, methods=['get'])
    def paiements(self, request, pk=None):
        facture = self.get_object()
        serializer = PaiementFournisseurSerializer(facture.paiements.all(), many=True)
        return Response(serializer.data)


class PaiementFournisseurViewSet(viewsets.ModelViewSet):
    queryset = PaiementFournisseur.objects.all().order_by('-date_paiement')
    serializer_class = PaiementFournisseurSerializer
