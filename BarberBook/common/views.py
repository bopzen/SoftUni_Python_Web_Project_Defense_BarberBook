from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render

from BarberBook.barbershop.models import BarbershopProfile
from BarberBook.reservation.models import Reservation


def home_page(request):
    barbershops_count = BarbershopProfile.objects.all().count()
    reservations_count = Reservation.objects.all().count()
    context = {
        'barbershops_count': barbershops_count,
        'reservations_count': reservations_count,
    }
    return render(request, 'common/home.html', context)


def map_page(request):
    barbershops = BarbershopProfile.objects.all()
    context = {
        'barbershops': barbershops
    }
    return render(request, 'common/map-all-barbershops.html', context)


def search_view(request):
    if request.method == 'GET' and 'q' in request.GET:
        query = request.GET.get('q', '')
        results = BarbershopProfile.objects.filter(
            Q(name__icontains=query) | Q(city__icontains=query)
        )
        data = [{'name': result.name, 'address': result.address, 'city': result.city, 'slug': result.slug} for result in results]
        return JsonResponse(data, safe=False)
    return JsonResponse([], safe=False)


def about_page(request):
    return render(request, 'common/about.html')