from rest_framework import generics as api_views
from BarberBook.reservation.models import Reservation
from BarberBook.reservation.serializers import ReservationListSerializer


class ReservationListAPIView(api_views.ListAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationListSerializer
