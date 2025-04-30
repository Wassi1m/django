from django import forms
from .models import Chambre, TypeChambre

class TypeChambreForm(forms.ModelForm):
    class Meta:
        model = TypeChambre
        fields = ['nom', 'description', 'prix_par_nuit']

class ChambreForm(forms.ModelForm):
    class Meta:
        model = Chambre
        fields = ['numero', 'etage', 'type_chambre', 'capacite', 'statut', 'description'] 