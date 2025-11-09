from rest_framework import viewsets
from .models import BonCommande
from .serializers import BonCommandeSerializer


class BonCommandeViewSet(viewsets.ModelViewSet):
    queryset = BonCommande.objects.all().order_by('-date_commande')
    serializer_class = BonCommandeSerializer
