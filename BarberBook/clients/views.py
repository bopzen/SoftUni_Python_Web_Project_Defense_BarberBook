from django.shortcuts import render


def register_client(request):
    return render(request, 'clients/register-client.html')


def login_client(request):
    return render(request, 'clients/login-client.html')


def edit_client(request):
    return render(request, 'clients/edit-client.html')


def delete_client(request):
    return render(request, 'clients/delete-client.html')


def client_details(request):
    return render(request, 'clients/client-details.html')