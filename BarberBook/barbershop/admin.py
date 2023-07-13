from django.contrib import admin

from BarberBook.barbershop.models import BarbershopProfile


@admin.register(BarbershopProfile)
class AdminBarbershopProfile(admin.ModelAdmin):
    list_display = ['name', 'city', 'user']
