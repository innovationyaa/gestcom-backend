from django.db import models

class Charge(models.Model):
    TYPE_CHOICES = [
        ('fournisseur', 'Charge fournisseur'),
        ('salariale', 'Charge salariale'),
        ('fixe', 'Charge fixe'),
        ('patronale', 'Charge patronale'),
    ]

    type_charge = models.CharField(max_length=20, choices=TYPE_CHOICES)
    libelle = models.CharField(max_length=255)
    montant_ht = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    montant_tva = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    montant_ttc = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    date_echeance = models.DateField(null=True, blank=True)
    mode_paiement = models.CharField(max_length=100, null=True, blank=True)
    est_paye = models.BooleanField(default=False)

    # Champs spécifiques aux charges salariales
    employe = models.CharField(max_length=100, null=True, blank=True)
    mois = models.CharField(max_length=20, null=True, blank=True)
    salaire_net = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    cnss = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    primes = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    autres = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    # Champs pour charges fixes
    categorie_fixe = models.CharField(max_length=50, null=True, blank=True)  # Ex: Loyer, Eau, etc.

    # Champs pour charges patronales
    remuneration_gerant = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.libelle} ({self.get_type_charge_display()})"
