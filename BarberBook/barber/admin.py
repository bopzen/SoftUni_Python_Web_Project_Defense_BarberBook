from django.contrib import admin

from BarberBook.barber.models import Barber


@admin.register(Barber)
class AdminBarber(admin.ModelAdmin):
    list_display = ['name', 'barbershop']
    list_filter = ['barbershop']
    list_display_links = ['name', 'barbershop']
    list_per_page = 50
    search_fields = ['name', 'barbershop__name']
    search_help_text = 'Search by Barber Name, Barbershop Name'
