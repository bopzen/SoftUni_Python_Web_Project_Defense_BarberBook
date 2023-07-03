
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('BarberBook.common.urls')),
    path('accounts/', include('BarberBook.accounts.urls')),
    path('barbers/', include('BarberBook.barbers.urls')),
    path('barbershops/', include('BarberBook.barbershops.urls')),
    path('clients/', include('BarberBook.clients.urls')),
    path('reservations/', include('BarberBook.reservations.urls')),
    path('reviews/', include('BarberBook.reviews.urls'))
]
