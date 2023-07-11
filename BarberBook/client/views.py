from django.shortcuts import render


def register_client(request):
    return render(request, 'client/register-client.html')


def login_client(request):
    return render(request, 'client/login-client.html')


def edit_client(request):
    return render(request, 'client/edit-client.html')


def delete_client(request):
    return render(request, 'client/delete-client.html')


def client_details(request):
    return render(request, 'client/client-details.html')