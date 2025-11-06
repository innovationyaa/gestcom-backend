from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FournisseurViewSet, FactureFournisseurViewSet, PaiementFournisseurViewSet

router = DefaultRouter()
router.register('fournisseurs', FournisseurViewSet)
router.register('factures-fournisseurs', FactureFournisseurViewSet)
router.register('paiements-fournisseurs', PaiementFournisseurViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
