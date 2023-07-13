from django.db import models

from BarberBook.barbershop.models import BarbershopProfile


class Barber(models.Model):
    name = models.CharField(
        max_length=30,
        null=False,
        blank=False
    )
    about = models.TextField(
        null=False,
        blank=False
    )
    barber_picture = models.ImageField(
        upload_to='barber-profile-pictures',
        null=True,
        blank=True,
    )
    barbershop = models.ForeignKey(
        BarbershopProfile,
        on_delete=models.DO_NOTHING
    )

    def __str__(self):
        return self.name
