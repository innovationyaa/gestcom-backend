from django.db import models

class Fournisseur(models.Model):
    nom = models.CharField(max_length=100)
    contact = models.CharField(max_length=50)
    adresse = models.TextField(blank=True, null=True)
    ice = models.CharField(max_length=20, unique=True)
    if_fiscal = models.CharField(max_length=20, unique=True)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom


class FactureFournisseur(models.Model):
    STATUT_CHOICES = [
        ('non_payee', 'Non payée'),
        ('partielle', 'Partielle'),
        ('payee', 'Payée'),
    ]

    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE, related_name='factures')
    numero_facture = models.CharField(max_length=50, unique=True)
    date_facture = models.DateField()
    montant_ht = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    tva = models.DecimalField(max_digits=5, decimal_places=2, default=20)
    montant_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    paiement_restant = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='non_payee')
    date_echeance = models.DateField(null=True, blank=True)
    notes = models.TextField(blank=True, null=True)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.numero_facture} - {self.fournisseur.nom}"

    def mettre_a_jour_statut(self):
        total_paye = sum(p.montant for p in self.paiements.all())
        if total_paye >= self.montant_total:
            self.statut = 'payee'
        elif total_paye > 0:
            self.statut = 'partielle'
        else:
            self.statut = 'non_payee'
        self.paiement_restant = self.montant_total - total_paye
        self.save()


class PaiementFournisseur(models.Model):
    facture = models.ForeignKey(FactureFournisseur, on_delete=models.CASCADE, related_name='paiements')
    date_paiement = models.DateField()
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    mode_paiement = models.CharField(max_length=50, blank=True, null=True)
    reference_paiement = models.CharField(max_length=100, blank=True, null=True)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Paiement {self.montant} pour {self.facture.numero_facture}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.facture.mettre_a_jour_statut()
