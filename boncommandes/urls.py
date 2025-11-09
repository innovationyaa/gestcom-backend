from rest_framework.routers import DefaultRouter
from .views import BonCommandeViewSet

router = DefaultRouter()
router.register(r'boncommandes', BonCommandeViewSet, basename='boncommande')

urlpatterns = router.urls
