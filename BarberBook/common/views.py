from django.shortcuts import render

from BarberBook.barbershop.models import BarbershopProfile
from BarberBook.reservation.models import Reservation


def home_page(request):
    barbershops_count = BarbershopProfile.objects.all().count()
    reservations_count = Reservation.objects.all().count()
    context = {
        'barbershops_count': barbershops_count,
        'reservations_count': reservations_count
    }
    return render(request, 'common/home.html', context)


def map_page(request):
    barbershops = BarbershopProfile.objects.all()
    context = {
        'barbershops': barbershops
    }
    return render(request, 'common/map-all-barbershops.html', context)