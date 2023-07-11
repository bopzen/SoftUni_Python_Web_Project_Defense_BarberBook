from django.shortcuts import render


def register_barbershop(request):
    return render(request, 'barbershop/register-barbershop.html')


def login_barbershop(request):
    return render(request, 'barbershop/login-barbershop.html')


def edit_barbershop(request):
    return render(request, 'barbershop/edit-barbershop.html')


def delete_barbershop(request):
    return render(request, 'barbershop/delete-barbershop.html')


def barbershop_details(request):
    return render(request, 'barbershop/barbershop-details.html')


def barbershops_list(request):
    return render(request, 'barbershop/barbershops-list.html')