from django.urls import path, include

from BarberBook.barbershop.views import register_barbershop, login_barbershop, edit_barbershop, delete_barbershop, \
    barbershop_details, barbershops_list

urlpatterns = [
    path('all/', barbershops_list, name='barbershop-list'),
    path('barbershop/', include([
        path('register/', register_barbershop, name='register-barbershop'),
        path('login/', login_barbershop, name='login-barbershop'),
        path('edit/', edit_barbershop, name='edit-barbershop'),
        path('delete/', delete_barbershop, name='delete-barbershop'),
        path('details/', barbershop_details, name='barbershop-details')
    ]))
]