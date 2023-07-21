from django.contrib import admin

from BarberBook.review.models import Review


@admin.register(Review)
class AdminReview(admin.ModelAdmin):
    list_display = ['pk', 'user', 'barbershop', 'date_created', 'rating', 'comment']
