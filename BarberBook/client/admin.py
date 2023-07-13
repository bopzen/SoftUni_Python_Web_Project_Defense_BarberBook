from django.contrib import admin

from BarberBook.client.models import ClientProfile


@admin.register(ClientProfile)
class AdminClientProfile(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'city', 'phone', 'user']
