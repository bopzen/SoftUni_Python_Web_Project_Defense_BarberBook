from django.urls import path
from BarberBook.client.views import EditClientProfileView, ClientProfileDetailsView

urlpatterns = [
    path('edit/', EditClientProfileView.as_view(), name='edit-client'),
    path('profile/', ClientProfileDetailsView.as_view(), name='client-details')
]