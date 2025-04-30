from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['client', 'chambre', 'date_arrivee', 'date_depart', 'nombre_personnes', 'commentaires']
        widgets = {
            'date_arrivee': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'date_depart': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        } 