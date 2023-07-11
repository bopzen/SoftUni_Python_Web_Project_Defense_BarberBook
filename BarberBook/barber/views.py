from django.shortcuts import render


def add_barber(request):
    return render(request, 'barber/create-barber.html')


def edit_barber(request):
    return render(request, 'barber/edit-barber.html')


def delete_barber(request):
    return render(request, 'barber/delete-barber.html')


def barber_details(request):
    return render(request, 'barber/barber-details.html')


def barbers_list(request):
    return render(request, 'barber/barbers-list.html')