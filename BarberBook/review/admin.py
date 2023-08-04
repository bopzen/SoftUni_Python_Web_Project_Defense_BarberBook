from django.contrib import admin

from BarberBook.review.models import Review


@admin.register(Review)
class AdminReview(admin.ModelAdmin):
    list_display = ['user', 'barbershop', 'date_created', 'rating', 'comment']
    list_display_links = ['user', 'barbershop', 'date_created', 'rating', 'comment']
    list_filter = ['barbershop', 'date_created', 'rating']
    list_per_page = 50
    search_fields = ['user__username', 'barbershop__name', 'rating']
    search_help_text = 'Search by Username, Barbershop Name, Rating'
