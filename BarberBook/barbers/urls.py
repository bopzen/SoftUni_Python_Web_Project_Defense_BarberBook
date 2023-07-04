from django.urls import path, include

from BarberBook.barbers.views import add_barber, edit_barber, delete_barber, barber_details, barbers_list

urlpatterns = [
    path('all/', barbers_list, name='barbers-list'),
    path('barber/', include([
        path('add/', add_barber, name='create-barber'),
        path('edit/', edit_barber, name='edit-barber'),
        path('delete/', delete_barber, name='delete-barber'),
        path('details/', barber_details, name='barber-details')
    ]))
]