from django.contrib.auth import get_user_model
from django.db import models

from BarberBook.barbershop.models import BarbershopProfile

UserModel = get_user_model()


class Review(models.Model):
    RATING_CHOICES = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    ]

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
    barbershop = models.ForeignKey(
        BarbershopProfile,
        on_delete=models.CASCADE,
    )
    rating = models.IntegerField(
        choices=RATING_CHOICES,
    )
    comment = models.TextField()

    def __str__(self):
        return f'Review by {self.user} for {self.barbershop.name}'
