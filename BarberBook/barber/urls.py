from django.urls import path, include

from BarberBook.barber.views import CreateBarberView, EditBarberView, DeleteBarberView, BarberDetailsView

urlpatterns = [
    path('create/', CreateBarberView.as_view(), name='create-barber'),
    path('<int:pk>/edit/', EditBarberView.as_view(), name='edit-barber'),
    path('<int:pk>/delete/', DeleteBarberView.as_view(), name='delete-barber'),
    path('<int:pk>/details/', BarberDetailsView.as_view(), name='barber-details')
]