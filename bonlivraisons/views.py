from rest_framework import viewsets
from .models import BonLivraison
from .serializers import BonLivraisonSerializer


class BonLivraisonViewSet(viewsets.ModelViewSet):
    queryset = BonLivraison.objects.all().order_by('-date_livraison')
    serializer_class = BonLivraisonSerializer
