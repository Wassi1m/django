from django.db import models

class TypeChambre(models.Model):
    nom = models.CharField(max_length=50)
    description = models.TextField()
    prix_par_nuit = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.nom

class Chambre(models.Model):
    numero = models.CharField(max_length=10, unique=True)
    etage = models.ForeignKey('etages.Etage', on_delete=models.CASCADE)
    type_chambre = models.ForeignKey(TypeChambre, on_delete=models.CASCADE)
    capacite = models.IntegerField()
    statut = models.CharField(max_length=20, choices=[
        ('disponible', 'Disponible'),
        ('occupee', 'Occupée'),
        ('maintenance', 'En maintenance'),
        ('nettoyage', 'En nettoyage')
    ])
    description = models.TextField()
    
    def __str__(self):
        return f"Chambre {self.numero} - {self.type_chambre.nom}" 