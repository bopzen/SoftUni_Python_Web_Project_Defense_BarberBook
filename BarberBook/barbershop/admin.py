from django.contrib import admin

from BarberBook.barbershop.models import BarbershopProfile, ServiceCategory, BarbershopService, BarbershopWorkingHours


@admin.register(BarbershopProfile)
class AdminBarbershopProfile(admin.ModelAdmin):
    list_display = ['pk', 'name', 'city', 'user']


@admin.register(ServiceCategory)
class AdminServiceCategory(admin.ModelAdmin):
    pass

@admin.register(BarbershopService)
class AdminBarbershopService(admin.ModelAdmin):
    pass

@admin.register(BarbershopWorkingHours)
class AdminBarbershopWorkingHours(admin.ModelAdmin):
    pass