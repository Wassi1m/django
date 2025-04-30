from django.contrib import admin
from .models import Etage

@admin.register(Etage)
class EtageAdmin(admin.ModelAdmin):
    list_display = ('numero', 'designation') 