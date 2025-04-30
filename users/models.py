from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    telephone = models.CharField(max_length=15)
    adresse = models.TextField()
    role = models.CharField(max_length=20, choices=[
        ('admin', 'Administrateur'),
        ('receptionniste', 'Réceptionniste'),
        ('femme_chambre', 'Femme de Chambre'),
        ('client', 'Client')
    ])
    date_creation = models.DateTimeField(auto_now_add=True)

    # Ajout des related_name pour éviter les conflits
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    ) 