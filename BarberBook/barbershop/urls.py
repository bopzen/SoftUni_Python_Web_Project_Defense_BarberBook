from django.urls import path, include

from BarberBook.barbershop.views import EditBarbershopProfileView, BarbershopProfileDetailsView, barbershop_list, \
    CreateBarbershopServiceView, EditBarbershopServiceView, DeleteBarbershopServiceView, BarbershopServicesDetailsView

urlpatterns = [
    path('<slug:slug>/edit/', EditBarbershopProfileView.as_view(), name='edit-barbershop'),
    path('<slug:slug>/profile/', BarbershopProfileDetailsView.as_view(), name='barbershop-details'),
    path('<slug:slug>/service/', include([
        path('create/', CreateBarbershopServiceView.as_view(), name='create-service'),
        path('<int:pk>/edit/', EditBarbershopServiceView.as_view(), name='edit-service'),
        path('<int:pk>/delete/', DeleteBarbershopServiceView.as_view(), name='delete-service'),
        path('<int:pk>/details/', BarbershopServicesDetailsView.as_view(), name='service-details'),
    ])),
    path('all/', barbershop_list, name='barbershop-list')
]