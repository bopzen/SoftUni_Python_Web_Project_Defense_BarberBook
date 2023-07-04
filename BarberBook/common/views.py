from django.shortcuts import render


def home_page(request):
    return render(request, 'common/home.html')


def register_page(request):
    return render(request, 'common/register.html')


def login_page(request):
    return render(request, 'common/login.html')


def logout_page(request):
    return render(request, 'common/logout.html')


def profile_page(request):
    return render(request, 'common/profile.html')
