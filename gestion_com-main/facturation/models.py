from django.db import models
from decimal import Decimal

class Facture(models.Model):
    STATUTS = [
        ('payee', 'Payée'),
        ('impayee', 'Impayée'),
        ('partielle', 'Partielle'),
    ]

    numero = models.CharField(max_length=50, unique=True)
    date_emission = models.DateField(auto_now_add=True)
    date_echeance = models.DateField(null=True, blank=True)
    client = models.ForeignKey('clients.Client', on_delete=models.CASCADE, related_name='factures')
    devis = models.ForeignKey('devis.Devis', on_delete=models.SET_NULL, null=True, blank=True)
    montant_ht = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    montant_ttc = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    statut = models.CharField(max_length=20, choices=STATUTS, default='impayee')

    def __str__(self):
        return f"Facture {self.numero} - {self.client}"

    def calculer_totaux(self):
        """Calcule automatiquement les montants HT et TTC à partir des lignes"""
        lignes = self.lignes.all()
        total_ht = Decimal('0.00')
        total_ttc = Decimal('0.00')
        for ligne in lignes:
            total_ht += ligne.quantite * ligne.prix_unitaire
            total_ttc += ligne.total_ttc
        self.montant_ht = total_ht
        self.montant_ttc = total_ttc
        self.save()


class LigneFacture(models.Model):
    facture = models.ForeignKey(Facture, on_delete=models.CASCADE, related_name='lignes')
    article = models.ForeignKey('stock.Article', on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField()
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2)
    tva = models.DecimalField(max_digits=5, decimal_places=2, default=20)

    @property
    def total_ttc(self):
        return (self.quantite * self.prix_unitaire) * (1 + self.tva / 100)

    def __str__(self):
        return f"{self.article} ({self.quantite})"
