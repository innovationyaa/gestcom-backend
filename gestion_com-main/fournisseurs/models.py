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
