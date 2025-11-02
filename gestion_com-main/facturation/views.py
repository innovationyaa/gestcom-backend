from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Facture, LigneFacture
from .serializers import FactureSerializer, LigneFactureSerializer

class FactureViewSet(viewsets.ModelViewSet):
    queryset = Facture.objects.all().order_by('-date_emission')
    serializer_class = FactureSerializer

    @action(detail=True, methods=['post'])
    def changer_statut(self, request, pk=None):
        """
        Permet de modifier le statut d'une facture : payée, impayée, partielle
        """
        facture = self.get_object()
        statut = request.data.get('statut')
        if statut in ['payee', 'impayee', 'partielle']:
            facture.statut = statut
            facture.save()
            return Response({'message': f'Statut modifié à {statut}'}, status=status.HTTP_200_OK)
        return Response({'error': 'Statut invalide'}, status=status.HTTP_400_BAD_REQUEST)

class LigneFactureViewSet(viewsets.ModelViewSet):
    queryset = LigneFacture.objects.all()
    serializer_class = LigneFactureSerializer
