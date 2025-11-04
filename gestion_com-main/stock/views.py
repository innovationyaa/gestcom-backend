from rest_framework import viewsets
from .models import Categorie, SousCategorie, Article, MouvementStock
from .serializers import (
    CategorieWithSousCategoriesSerializer,
    SousCategorieSerializer,
    ArticleSerializer,
    MouvementStockSerializer
)


class CategorieViewSet(viewsets.ModelViewSet):
    queryset = Categorie.objects.prefetch_related('sous_categories').all()
    serializer_class = CategorieWithSousCategoriesSerializer


class SousCategorieViewSet(viewsets.ModelViewSet):
    queryset = SousCategorie.objects.select_related('categorie').all()
    serializer_class = SousCategorieSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class MouvementStockViewSet(viewsets.ModelViewSet):
    queryset = MouvementStock.objects.all()
    serializer_class = MouvementStockSerializer
