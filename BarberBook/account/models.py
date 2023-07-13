from django.contrib.auth.models import AbstractUser
from django.db import models


class AppUser(AbstractUser):
    ROLES = (
        ('Client', 'Client'),
        ('Barbershop', 'Barbershop')
    )

    role = models.CharField(
        max_length=10,
        choices=ROLES,
        blank=True
    )

