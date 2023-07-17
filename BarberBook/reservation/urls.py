from django.urls import path, include
from BarberBook.reservation.views import CreateReservation

urlpatterns = [
    path('create/<slug:slug>/', CreateReservation.as_view(), name='create-reservation')
]
