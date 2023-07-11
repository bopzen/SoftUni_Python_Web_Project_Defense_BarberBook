from django.urls import path

from BarberBook.barbershop.views import EditBarbershopProfileView, BarbershopProfileDetailsView, barbershop_list

urlpatterns = [
    path('<int:pk>/edit/', EditBarbershopProfileView.as_view(), name='edit-barbershop'),
    path('<int:pk>/<str:username>/profile/', BarbershopProfileDetailsView.as_view(), name='barbershop-details'),
    path('all/', barbershop_list, name='barbershop-list')
]