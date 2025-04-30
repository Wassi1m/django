from django.contrib import admin
from .models import Chambre, TypeChambre

@admin.register(Chambre)
class ChambreAdmin(admin.ModelAdmin):
    list_display = ('numero', 'type_chambre', 'etage', 'capacite', 'statut')
    list_filter = ('type_chambre', 'etage', 'statut')
    search_fields = ('numero', 'description')

@admin.register(TypeChambre)
class TypeChambreAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prix_par_nuit') 