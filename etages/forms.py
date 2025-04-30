from django import forms
from .models import Etage

class EtageForm(forms.ModelForm):
    class Meta:
        model = Etage
        fields = ['numero', 'designation', 'description'] 