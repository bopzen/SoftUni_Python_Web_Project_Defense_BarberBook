
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('BarberBook.common.urls')),
    path('account/', include('BarberBook.account.urls')),
    path('barber/', include('BarberBook.barber.urls')),
    path('barbershop/', include('BarberBook.barbershop.urls')),
    path('client/', include('BarberBook.client.urls')),
    path('reservation/', include('BarberBook.reservation.urls')),
    path('review/', include('BarberBook.review.urls'))
]
