from django import forms
from .models import Materiel

class MaterielForm(forms.ModelForm):
    class Meta:
        model = Materiel
        fields = ['nom', 'description', 'quantite', 'chambre', 'date_acquisition', 'etat'] 