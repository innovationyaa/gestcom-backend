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

    def verifier_statut(self):
        """
        Compare la quantité totale livrée avec celle commandée.
        Si tout est livré, le statut devient 'complete'.
        """
        total_bc = sum(dbc.quantite for dbc in self.bon_commande.details.all())
        total_bl = sum(dbl.quantite for dbl in self.details.all())

        ancien_statut = self.statut
        self.statut = 'complete' if total_bl >= total_bc else 'partielle'
        self.save()

        # ✅ Si le BL devient complet et que ce n’était pas le cas avant, créer les mouvements
        if ancien_statut != 'complete' and self.statut == 'complete':
            self.creer_mouvements_stock()

    def creer_mouvements_stock(self):
        """Crée un mouvement de stock pour chaque article du BL"""
        for detail in self.details.all():
            MouvementStock.objects.create(
                article=detail.article,
                type_mouvement=MouvementStock.ENTREE,
                quantite=detail.quantite,
                remarque=f"Réception complète via BL {self.numero_bl}"
            )


class DetailsBL(models.Model):
    bon_livraison = models.ForeignKey(BonLivraison, on_delete=models.CASCADE, related_name='details')
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.article.nom} ({self.quantite})"

    def save(self, *args, **kwargs):
        """
        Quand on ajoute un détail, on recalcule automatiquement le statut du BL.
        Les mouvements de stock seront créés uniquement quand le BL devient 'complet'.
        """
        super().save(*args, **kwargs)
        self.bon_livraison.verifier_statut()
