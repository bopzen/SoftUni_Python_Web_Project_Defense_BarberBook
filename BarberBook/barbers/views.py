from django.shortcuts import render


def add_barber(request):
    return render(request, 'barbers/create-barber.html')


def edit_barber(request):
    return render(request, 'barbers/edit-barber.html')


def delete_barber(request):
    return render(request, 'barbers/delete-barber.html')


def barber_details(request):
    return render(request, 'barbers/barber-details.html')


def barbers_list(request):
    return render(request, 'barbers/barbers-list.html')