from django.db import models

class Etage(models.Model):
    numero = models.IntegerField(unique=True)
    designation = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return f"Étage {self.numero} - {self.designation}" 