from django.urls import path

from BarberBook.barbershop.views import EditBarbershopProfileView, BarbershopProfileDetailsView, barbershop_list

urlpatterns = [
    path('<slug:slug>/edit/', EditBarbershopProfileView.as_view(), name='edit-barbershop'),
    path('<slug:slug>/profile/', BarbershopProfileDetailsView.as_view(), name='barbershop-details'),
    path('all/', barbershop_list, name='barbershop-list')
]