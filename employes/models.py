from django.db import models

class Employe(models.Model):
    nom = models.CharField(max_length=100)
    poste = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nom
