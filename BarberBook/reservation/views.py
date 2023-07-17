from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic as views

from BarberBook.barbershop.models import BarbershopProfile
from BarberBook.reservation.models import Reservation



