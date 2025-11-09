from django.db import models
from clients.models import Client
from stock.models import Article


class Devis(models.Model):
    STATUTS = [
        ("BROUILLON", "Brouillon"),
        ("VALIDE", "Validé"),
        ("REFUSE", "Refusé"),
    ]

    numero = models.CharField(max_length=20, unique=True)
    date = models.DateField(auto_now_add=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='devis')
    statut = models.CharField(max_length=20, choices=STATUTS, default="BROUILLON")
    remise = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    taxe = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_ht = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_ttc = models.DecimalField(max_digits=10, decimal_places=2, default=0)

# ✅ AJOUT ICI
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        null=True,   # ← important
        blank=True,  # ← important
        related_name="devis"

)
    def __str__(self):
        return f"Devis {self.numero}"  


class LigneDevis(models.Model):
    devis = models.ForeignKey(Devis, on_delete=models.CASCADE, related_name="lignes")
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField()
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2)
    tva = models.DecimalField(max_digits=5, decimal_places=2, default=20)

    def __str__(self):
        return f"{self.article.nom} x {self.quantite}"
