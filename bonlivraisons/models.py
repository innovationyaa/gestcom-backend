# bonlivraisons/models.py
from django.db import models
from boncommandes.models import BonCommande
from stock.models import Article, MouvementStock


class BonLivraison(models.Model):
    numero_bl = models.CharField(max_length=50, unique=True)
    bon_commande = models.ForeignKey(BonCommande, on_delete=models.CASCADE, related_name='bons_livraison')
    date_livraison = models.DateField(auto_now_add=True)
    statut = models.CharField(
        max_length=20,
        choices=[('partielle', 'Partielle'), ('complete', 'Complète')],
        default='partielle'
    )

    def __str__(self):
        return f"BL {self.numero_bl} - {self.bon_commande.fournisseur.nom}"

    def creer_mouvements_stock(self):
        """Créer un mouvement de stock pour chaque article du BL"""
        for detail in self.details.all():
            MouvementStock.objects.create(
                article=detail.article,
                type_mouvement=MouvementStock.ENTREE,
                quantite=detail.quantite,
                remarque=f"Ajout via BL {self.numero_bl} (BC {self.bon_commande.numero_bc})",
                bon_livraison=self.numero_bl,
                bon_commande=self.bon_commande.numero_bc
            )

    def save(self, *args, **kwargs):
        """Quand on enregistre un BL, on crée les mouvements correspondants"""
        super().save(*args, **kwargs)
        self.creer_mouvements_stock()


class DetailsBL(models.Model):
    bon_livraison = models.ForeignKey(BonLivraison, on_delete=models.CASCADE, related_name='details')
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.article.reference} ({self.quantite})"
