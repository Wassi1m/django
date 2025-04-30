from django.contrib import admin
from .models import Materiel

@admin.register(Materiel)
class MaterielAdmin(admin.ModelAdmin):
    list_display = ('nom', 'chambre', 'quantite', 'etat')
    list_filter = ('etat', 'chambre') 