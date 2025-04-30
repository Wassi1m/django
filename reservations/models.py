from django.db import models

class Reservation(models.Model):
    client = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    chambre = models.ForeignKey('chambres.Chambre', on_delete=models.CASCADE)
    date_arrivee = models.DateTimeField()
    date_depart = models.DateTimeField()
    nombre_personnes = models.IntegerField()
    statut = models.CharField(max_length=20, choices=[
        ('confirmee', 'Confirmée'),
        ('en_cours', 'En cours'),
        ('terminee', 'Terminée'),
        ('annulee', 'Annulée')
    ])
    commentaires = models.TextField(blank=True)
    
    def __str__(self):
        return f"Réservation {self.client.username} - Chambre {self.chambre.numero}" 