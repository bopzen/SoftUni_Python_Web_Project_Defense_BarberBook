from django.contrib import admin

from BarberBook.barber.models import Barber


@admin.register(Barber)
class AdminBarber(admin.ModelAdmin):
    list_display = ['name', 'barbershop']
