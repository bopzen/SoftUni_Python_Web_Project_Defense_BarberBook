from django.shortcuts import render


def edit_client(request):
    return render(request, 'client/edit-client.html')


def delete_client(request):
    return render(request, 'client/delete-client.html')


def client_details(request):
    return render(request, 'client/client-details.html')