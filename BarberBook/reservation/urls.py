from django.urls import path, include

from BarberBook.reservation.api_views import ReservationListAPIView
from BarberBook.reservation.views import select_barbershop, select_barbershop_service, select_barber, select_date, \
    select_time, create_reservation, reservation_success, ReservationsListView, DeleteReservationView

urlpatterns = [
    path('create/', include([
        path('select-barbershop/<slug:slug>/', select_barbershop, name='step1-select-barbershop'),
        path('select-barbershop-service/', select_barbershop_service, name='step2-select-barbershop-service'),
        path('select-barber/', select_barber, name='step3-select-barber'),
        path('select-date/', select_date, name='step4-select-date'),
        path('select-time/', select_time, name='step5-select-time'),
        path('confirm-reservation/', create_reservation, name='create-reservation'),
        path('reservation-success/', reservation_success, name='reservation-success')
    ])),
    path('reservations-list/<int:pk>/', ReservationsListView.as_view(), name='reservation-list'),
    path('delete/<int:pk>/', DeleteReservationView.as_view(), name='delete-reservation'),
    path('api/all-reservations/', ReservationListAPIView.as_view(), name='all-reservations-api')
]
