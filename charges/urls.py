from rest_framework import routers
from .views import ChargeViewSet

router = routers.DefaultRouter()
router.register(r'charges', ChargeViewSet, basename='charges')

urlpatterns = router.urls
