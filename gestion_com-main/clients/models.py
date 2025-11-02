from django.db import models

class Client(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    adresse = models.TextField(blank=True, null=True)
    statut = models.CharField(
        max_length=10,
        choices=[('ACTIF', 'Actif'), ('INACTIF', 'Inactif')],
        default='ACTIF'
    )

    def __str__(self):
        return self.nom
