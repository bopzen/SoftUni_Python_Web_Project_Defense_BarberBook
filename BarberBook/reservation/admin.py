from django.contrib import admin

from BarberBook.reservation.models import Reservation


@admin.register(Reservation)
class AdminReservation(admin.ModelAdmin):
    list_display = ['pk', 'date', 'time', 'barber', 'barbershop', 'user', 'service']
