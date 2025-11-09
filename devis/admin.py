from django.contrib import admin
from .models import Devis, LigneDevis

class LigneDevisInline(admin.TabularInline):
    model = LigneDevis
    extra = 1


@admin.register(Devis)
class DevisAdmin(admin.ModelAdmin):
    list_display = ('numero', 'client', 'date', 'statut')  # client réactivé
    list_filter = ('statut', 'date')
    search_fields = ('numero', 'client__nom')  #  recherche par nom de client
    inlines = [LigneDevisInline]
