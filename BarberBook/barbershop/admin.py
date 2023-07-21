from django.contrib import admin

from BarberBook.barbershop.models import BarbershopProfile, ServiceCategory, BarbershopService, BarbershopWorkingHours, \
    BarbershopPicture


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
    list_display = ['pk', 'barbershop', 'day', 'start_time', 'end_time']
    list_filter = ['barbershop']

@admin.register(BarbershopPicture)
class AdminBarbershopPicture(admin.ModelAdmin):
    pass
