from rest_framework.routers import DefaultRouter
from .views import BonLivraisonViewSet

router = DefaultRouter()
router.register(r'bonlivraisons', BonLivraisonViewSet, basename='bonlivraison')

urlpatterns = router.urls
