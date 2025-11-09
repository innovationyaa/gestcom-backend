from django.db import models
from fournisseurs.models import Fournisseur
from stock.models import Article


class BonCommande(models.Model):
    STATUT_CHOICES = [
        ('en_attente', 'En attente'),
        ('validee', 'Validée'),
        ('livree', 'Livrée'),
        ('annulee', 'Annulée'),
    ]

    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE, related_name='bons_commandes')
    numero_bc = models.CharField(max_length=50, unique=True)
    date_commande = models.DateField(auto_now_add=True)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='en_attente')
    montant_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"BC {self.numero_bc} - {self.fournisseur.nom}"

    def calculer_total(self):
        total = sum(detail.prix_total for detail in self.details.all())
        self.montant_total = total
        self.save()


class DetailsBC(models.Model):
    bon_commande = models.ForeignKey(BonCommande, on_delete=models.CASCADE, related_name='details')
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField()
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2)
    prix_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        self.prix_total = self.quantite * self.prix_unitaire
        super().save(*args, **kwargs)
        self.bon_commande.calculer_total()

    def __str__(self):
        return f"{self.article.reference} x{self.quantite}"
