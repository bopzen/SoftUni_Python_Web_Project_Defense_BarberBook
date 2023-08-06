from django.core import validators
from django.db import models

from BarberBook.barber.validators import validate_name, validate_barber_picture_file_size
from BarberBook.barbershop.models import BarbershopProfile


class Barber(models.Model):
    MIN_LENGTH_NAME = 2
    MAX_LENGTH_NAME = 30
    name = models.CharField(
        max_length=MAX_LENGTH_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LENGTH_NAME),
            validate_name
        ),
        null=False,
        blank=False
    )
    about = models.TextField(
        null=False,
        blank=False
    )
    barber_picture = models.ImageField(
        upload_to='barber-profile-pictures',
        validators=(validate_barber_picture_file_size,),
        null=True,
        blank=True,
    )
    barbershop = models.ForeignKey(
        BarbershopProfile,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
