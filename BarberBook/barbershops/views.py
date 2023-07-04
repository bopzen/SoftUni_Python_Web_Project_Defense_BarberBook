from django.shortcuts import render


def register_barbershop(request):
    return render(request, 'barbershops/register-barbershop.html')


def login_barbershop(request):
    return render(request, 'barbershops/login-barbershop.html')


def edit_barbershop(request):
    return render(request, 'barbershops/edit-barbershop.html')


def delete_barbershop(request):
    return render(request, 'barbershops/delete-barbershop.html')


def barbershop_details(request):
    return render(request, 'barbershops/barbershop-details.html')


def barbershops_list(request):
    return render(request, 'barbershops/barbershops-list.html')