from django.urls import path, include

from BarberBook.barbershop.views import edit_barbershop, delete_barbershop, \
    barbershop_details, barbershops_list

urlpatterns = [
    path('all/', barbershops_list, name='barbershop-list'),
    path('barbershop/', include([
        path('edit/', edit_barbershop, name='edit-barbershop'),
        path('delete/', delete_barbershop, name='delete-barbershop'),
        path('details/', barbershop_details, name='barbershop-details')
    ]))
]