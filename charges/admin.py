from django.contrib import admin
from .models import Charge

@admin.register(Charge)
class ChargeAdmin(admin.ModelAdmin):
    list_display = (
        'libelle',
        'type_charge',
        'montant_ht',
        'montant_tva',
        'montant_ttc',
        'date_echeance',
        'mode_paiement',
        'est_paye',
    )
    list_filter = ('type_charge', 'est_paye', 'mode_paiement')
    search_fields = ('libelle', 'type_charge')
    ordering = ('-date_creation',)

    fieldsets = (
        ('Informations générales', {
            'fields': ('type_charge', 'libelle', 'montant_ht', 'montant_tva', 'montant_ttc')
        }),
        ('Paiement', {
            'fields': ('date_echeance', 'mode_paiement', 'est_paye')
        }),
        ('Charge salariale (optionnel)', {
            'classes': ('collapse',),
            'fields': ('employe', 'mois', 'salaire_net', 'cnss', 'primes', 'autres')
        }),
        ('Charge fixe (optionnel)', {
            'classes': ('collapse',),
            'fields': ('categorie_fixe',)
        }),
        ('Charge patronale (optionnel)', {
            'classes': ('collapse',),
            'fields': ('remuneration_gerant',)
        }),
    )
