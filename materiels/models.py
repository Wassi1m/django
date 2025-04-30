from django.db import models

class Materiel(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    quantite = models.IntegerField()
    chambre = models.ForeignKey('chambres.Chambre', on_delete=models.CASCADE)
    date_acquisition = models.DateField()
    etat = models.CharField(max_length=20, choices=[
        ('neuf', 'Neuf'),
        ('bon', 'Bon état'),
        ('moyen', 'État moyen'),
        ('mauvais', 'Mauvais état')
    ])
    
    def __str__(self):
        return f"{self.nom} - Chambre {self.chambre.numero}" 