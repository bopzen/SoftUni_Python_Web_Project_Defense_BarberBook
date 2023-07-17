from django.db import models

from BarberBook.barber.models import Barber
from BarberBook.barbershop.models import BarbershopProfile, BarbershopService
from BarberBook.client.models import ClientProfile

from datetime import date, time, timedelta
from django.utils import timezone
from django.core import exceptions


class Reservation(models.Model):

    TIME_SLOT_CHOICES = []
    for hour in range(0, 24):
        for minute in range(0, 60, 30):
            time_slot = time(hour, minute)
            display_text = time_slot.strftime('%H:%M')
            TIME_SLOT_CHOICES.append((time_slot, display_text))

    client = models.ForeignKey(
        ClientProfile,
        on_delete=models.CASCADE
    )
    service = models.ForeignKey(
        BarbershopService,
        on_delete=models.CASCADE,
        limit_choices_to={'barbershop': models.OuterRef('barbershop')}
    )

    barbershop = models.ForeignKey(
        BarbershopProfile,
        on_delete=models.CASCADE
    )
    barber = models.ForeignKey(
        Barber,
        on_delete=models.CASCADE
    )
    date = models.DateField(
        null=False,
        blank=False
    )
    time = models.TimeField(
        choices=TIME_SLOT_CHOICES,
        null=False,
        blank=False,
    )

    def clean(self):
        current_datetime = timezone.now()
        reservation_datetime = timezone.datetime.combine(self.date, self.time)

        if reservation_datetime <= current_datetime:
            raise exceptions.ValidationError('Reservation datetime must be in the future.')

        max_date = current_datetime + timedelta(days=14)
        if self.date > max_date:
            raise exceptions.ValidationError('Reservation date must be within 14 days from now.')

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'Reservation for Client: {self.client} Barber: {self.barber} at {self.barbershop} on {self.date} {self.time}'
