from django.contrib import admin

from BarberBook.barbershop.models import BarbershopProfile, ServiceCategory


@admin.register(BarbershopProfile)
class AdminBarbershopProfile(admin.ModelAdmin):
    list_display = ['name', 'city', 'user']


@admin.register(ServiceCategory)
class AdminServiceCategory(admin.ModelAdmin):
    pass
