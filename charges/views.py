from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum
from .models import Charge
from .serializers import ChargeSerializer

class ChargeViewSet(viewsets.ModelViewSet):
    queryset = Charge.objects.all().order_by('-date_creation')
    serializer_class = ChargeSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['libelle', 'type_charge', 'mode_paiement']

    # Endpoint perso: statistiques
    @action(detail=False, methods=['get'])
    def stats(self, request):
        total_charges = Charge.objects.aggregate(total=Sum('montant_ttc'))['total'] or 0
        fournisseurs = Charge.objects.filter(type_charge='fournisseur').aggregate(total=Sum('montant_ttc'))['total'] or 0
        salariales = Charge.objects.filter(type_charge='salariale').aggregate(total=Sum('montant_ttc'))['total'] or 0
        fixes = Charge.objects.filter(type_charge='fixe').aggregate(total=Sum('montant_ttc'))['total'] or 0
        patronales = Charge.objects.filter(type_charge='patronale').aggregate(total=Sum('montant_ttc'))['total'] or 0

        return Response({
            "total_charges": total_charges,
            "charges_fournisseurs": fournisseurs,
            "charges_salariales": salariales,
            "charges_fixes": fixes,
            "charges_patronales": patronales
        })
