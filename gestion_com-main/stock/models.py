from django.db import models
from fournisseurs.models import Fournisseur


class Categorie(models.Model):
    nom = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.nom


class SousCategorie(models.Model):
    nom = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.nom


class Article(models.Model):
    reference = models.CharField(max_length=100, unique=True)
    categorie = models.ForeignKey(
        Categorie,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="articles"
    )
    sous_categorie = models.ForeignKey(
        SousCategorie,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="articles"
    )
    description = models.TextField(blank=True)
    quantite_actuelle = models.IntegerField(default=0)

    UNITE_CHOICES = [
        ('kg', 'Kilogramme'),
        ('g', 'Gramme'),
        ('l', 'Litre'),
        ('ml', 'Millilitre'),
        ('unité', 'Unité'),
        ('m', 'Mètre'),
        ('cm', 'Centimètre'),
    ]
    unite_mesure = models.CharField(
        max_length=20,
        choices=UNITE_CHOICES,
        default='unité'
    )

    prix_achat = models.DecimalField(max_digits=10, decimal_places=2)
    prix_vente = models.DecimalField(max_digits=10, decimal_places=2)
    seuil_minimum = models.IntegerField(default=0)
    image = models.ImageField(upload_to='articles/', blank=True, null=True)

    fournisseur = models.ForeignKey(
        Fournisseur,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="articles"
    )

    def __str__(self):
        fournisseur_nom = self.fournisseur.nom if self.fournisseur else "Aucun fournisseur"
        sous_cat_nom = self.sous_categorie.nom if self.sous_categorie else "Sans sous-catégorie"
        return f"{self.reference} - {sous_cat_nom} ({fournisseur_nom})"


class MouvementStock(models.Model):
    ENTREE = 'entrée'
    SORTIE = 'sortie'
    TYPE_CHOICES = [
        (ENTREE, 'Entrée'),
        (SORTIE, 'Sortie'),
    ]

    type_mouvement = models.CharField(max_length=10, choices=TYPE_CHOICES)
    quantite = models.PositiveIntegerField()
    remarque = models.TextField(blank=True)
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='mouvements'
    )
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.pk is None:  # seulement à la création
            if self.type_mouvement == self.ENTREE:
                self.article.quantite_actuelle += self.quantite
            elif self.type_mouvement == self.SORTIE:
                self.article.quantite_actuelle -= self.quantite
            self.article.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.type_mouvement} | {self.article.reference} | {self.quantite}"
