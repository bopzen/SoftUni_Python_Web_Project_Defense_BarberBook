from django.urls import path, include

from BarberBook.clients.views import register_client, login_client, edit_client, delete_client, client_details

urlpatterns = [
    path('client/', include([
        path('register/', register_client, name='register-client'),
        path('login/', login_client, name='login-client'),
        path('edit/', edit_client, name='edit-client'),
        path('delete/', delete_client, name='delete-client'),
        path('details/', client_details, name='client-details')
    ]))
]