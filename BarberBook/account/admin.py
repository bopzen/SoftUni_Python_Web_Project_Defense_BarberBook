from django.contrib import admin

from BarberBook.account.models import AppUser


@admin.register(AppUser)
class AdminAppUser(admin.ModelAdmin):
    pass
