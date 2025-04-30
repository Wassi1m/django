from django.contrib import admin
from .models import Reservation

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('client', 'chambre', 'date_arrivee', 'date_depart', 'statut')
    list_filter = ('statut', 'chambre') 