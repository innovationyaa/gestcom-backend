from rest_framework import viewsets
from .models import Devis
from .serializers import DevisSerializer
from rest_framework.permissions import IsAuthenticated

class DevisViewSet(viewsets.ModelViewSet):
    queryset = Devis.objects.all().order_by('-date')
    serializer_class = DevisSerializer
    permission_classes = [IsAuthenticated]
