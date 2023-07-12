from django.urls import path, include

from BarberBook.barber.views import CreateBarberView, edit_barber, delete_barber, barber_details, barbers_list

urlpatterns = [
    path('all/', barbers_list, name='barber-list'),
    path('create/', CreateBarberView.as_view(), name='create-barber'),
    path('edit/', edit_barber, name='edit-barber'),
    path('delete/', delete_barber, name='delete-barber'),
    path('details/', barber_details, name='barber-details')
]