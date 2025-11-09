from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Facture, LigneFacture
from .serializers import FactureSerializer, LigneFactureSerializer


class FactureViewSet(viewsets.ModelViewSet):
    queryset = Facture.objects.all().order_by('-date_emission')
    serializer_class = FactureSerializer

    @action(detail=True, methods=['post'])
    def calculer_totaux(self, request, pk=None):
        facture = self.get_object()
        facture.calculer_totaux()
        return Response({'message': 'Totaux mis à jour', 'montant_ttc': facture.montant_ttc})


class LigneFactureViewSet(viewsets.ModelViewSet):
    queryset = LigneFacture.objects.all()
    serializer_class = LigneFactureSerializer
