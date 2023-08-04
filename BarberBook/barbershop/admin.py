from django.contrib import admin

from BarberBook.barbershop.models import BarbershopProfile, ServiceCategory, BarbershopService, BarbershopWorkingHours, \
    BarbershopPicture


@admin.register(BarbershopProfile)
class AdminBarbershopProfile(admin.ModelAdmin):
    list_display = ['name', 'city', 'address', 'user']
    list_display_links = ['name', 'city', 'address', 'user']
    list_filter = ['city']
    list_per_page = 50
    search_fields = ['name', 'city', 'user__username']
    search_help_text = 'Search by Barbershop Name, City, Username'


@admin.register(ServiceCategory)
class AdminServiceCategory(admin.ModelAdmin):
    list_display = ['category_name']


@admin.register(BarbershopService)
class AdminBarbershopService(admin.ModelAdmin):
    list_display = ['barbershop', 'category', 'service_name', 'price']
    list_display_links = ['barbershop', 'category', 'service_name', 'price']
    list_filter = (
        ('barbershop', admin.RelatedFieldListFilter),
        ('category', admin.RelatedFieldListFilter),
        'price',
    )
    search_fields = ['barbershop__name', 'service_name', 'category__category_name', 'price']
    search_help_text = 'Search by Barbershop Name, Service Name, Category Name, Price'


@admin.register(BarbershopWorkingHours)
class AdminBarbershopWorkingHours(admin.ModelAdmin):
    list_display = ['barbershop', 'day', 'start_time', 'end_time']
    list_display_links = ['barbershop', 'day', 'start_time', 'end_time']
    list_filter = ['barbershop', 'day']
    list_per_page = 56
    search_fields = ['barbershop__name']
    search_help_text = 'Search by Barbershop Name'


@admin.register(BarbershopPicture)
class BarbershopPictureAdmin(admin.ModelAdmin):
    list_display = ['barbershop', 'image']
    list_display_links = ['barbershop', 'image']
    list_filter = ['barbershop']
    list_per_page = 50
    ordering = ['barbershop']
    search_fields = ['barbershop__name', 'image']
    search_help_text = 'Search by Barbershop Name, Image Name'


