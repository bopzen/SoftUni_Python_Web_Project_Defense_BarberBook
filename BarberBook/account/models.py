from django.contrib.auth.models import AbstractUser
from django.db import models


class AppUser(AbstractUser):
    MAX_LENGTH_ROLE = 10
    ROLES = (
        ('Client', 'Client'),
        ('Barbershop', 'Barbershop')
    )

    role = models.CharField(
        max_length=MAX_LENGTH_ROLE,
        choices=ROLES,
        blank=True
    )

