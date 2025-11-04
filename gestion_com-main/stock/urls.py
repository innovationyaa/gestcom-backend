from rest_framework.routers import DefaultRouter
from .views import (
    ArticleViewSet,
    MouvementStockViewSet,
    CategorieViewSet,
    SousCategorieViewSet
)

router = DefaultRouter()
router.register(r'articles', ArticleViewSet, basename='article')
router.register(r'mouvements', MouvementStockViewSet, basename='mouvement')
router.register(r'categories', CategorieViewSet, basename='categorie')
router.register(r'sous-categories', SousCategorieViewSet, basename='souscategorie')

urlpatterns = router.urls
