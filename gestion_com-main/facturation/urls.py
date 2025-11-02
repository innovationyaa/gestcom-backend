from rest_framework.routers import DefaultRouter
from .views import FactureViewSet, LigneFactureViewSet

router = DefaultRouter()
router.register(r'factures', FactureViewSet)
router.register(r'lignes-facture', LigneFactureViewSet)

urlpatterns = router.urls
