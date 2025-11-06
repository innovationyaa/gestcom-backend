from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FactureViewSet, LigneFactureViewSet

router = DefaultRouter()
router.register('factures', FactureViewSet)
router.register('lignes-facture', LigneFactureViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
