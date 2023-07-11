from django.urls import path, include

from BarberBook.client.views import edit_client, delete_client, client_details

urlpatterns = [
    path('client/', include([
        path('edit/', edit_client, name='edit-client'),
        path('delete/', delete_client, name='delete-client'),
        path('details/', client_details, name='client-details')
    ]))
]