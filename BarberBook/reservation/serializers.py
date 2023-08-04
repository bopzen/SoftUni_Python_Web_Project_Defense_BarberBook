from rest_framework import serializers
from BarberBook.reservation.models import Reservation


class ReservationListSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.username')
    barber_name = serializers.CharField(source='barber.name')
    barbershop_name = serializers.CharField(source='barbershop.name')
    service_name = serializers.CharField(source='service.service_name')

    class Meta:
        model = Reservation
        fields = ['id', 'user_name', 'barber_name', 'barbershop_name', 'service_name', 'date', 'time']