from django.db import models
from decimal import Decimal

class Facture(models.Model):
    STATUTS = [
        ('impayee', 'Impayée'),
        ('partielle', 'Partielle'),
        ('payee', 'Payée'),
    ]

    numero = models.CharField(max_length=50, unique=True)
    date_emission = models.DateField(auto_now_add=True)
    date_echeance = models.DateField(null=True, blank=True)
    client = models.ForeignKey('clients.Client', on_delete=models.CASCADE, related_name='factures')
    devis = models.ForeignKey('devis.Devis', on_delete=models.SET_NULL, null=True, blank=True)

    montant_ht = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    montant_ttc = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    remise = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    paiement_restant = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    moyen_paiement = models.CharField(max_length=50, blank=True, null=True)
    statut = models.CharField(max_length=20, choices=STATUTS, default='impayee')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Facture {self.numero} - {self.client}"

    def calculer_totaux(self):
        lignes = self.lignes.all()
        total_ht = Decimal('0.00')
        total_ttc = Decimal('0.00')
        for ligne in lignes:
            total_ht += ligne.total_ht
            total_ttc += ligne.total_ttc
        total_ht -= self.remise
        self.montant_ht = total_ht
        self.montant_ttc = total_ttc
        self.paiement_restant = total_ttc
        self.save()


class LigneFacture(models.Model):
    facture = models.ForeignKey(Facture, on_delete=models.CASCADE, related_name='lignes')
    article = models.ForeignKey('stock.Article', on_delete=models.CASCADE)
    description = models.CharField(max_length=255, blank=True, null=True)
    quantite = models.PositiveIntegerField()
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2)
    tva = models.DecimalField(max_digits=5, decimal_places=2, default=20)
    total_ht = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    @property
    def total_ttc(self):
        return (self.total_ht or self.quantite * self.prix_unitaire) * (1 + self.tva / 100)

    def save(self, *args, **kwargs):
        self.total_ht = self.quantite * self.prix_unitaire
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.article} ({self.quantite})"
