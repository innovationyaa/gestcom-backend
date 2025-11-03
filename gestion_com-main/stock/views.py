from rest_framework import viewsets
from .models import Article, MouvementStock, Categorie, SousCategorie
from .serializers import (
    ArticleSerializer,
    MouvementStockSerializer,
    CategorieSerializer,
    SousCategorieSerializer
)

# ---- Articles ----
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


# ---- Mouvements ----
class MouvementStockViewSet(viewsets.ModelViewSet):
    queryset = MouvementStock.objects.all()
    serializer_class = MouvementStockSerializer


# ---- Catégories ----
class CategorieViewSet(viewsets.ModelViewSet):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer


# ---- Sous-Catégories ----
class SousCategorieViewSet(viewsets.ModelViewSet):
    queryset = SousCategorie.objects.all()
    serializer_class = SousCategorieSerializer
