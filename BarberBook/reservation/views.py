import datetime

from datetime import datetime, timedelta
from django.utils import timezone

from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from BarberBook.barber.models import Barber
from BarberBook.barbershop.models import BarbershopProfile, BarbershopService
from BarberBook.reservation.forms import BarbershopServiceForm, BarbershopBarberForm, DateSelectionForm, \
    TimeSelectionForm, ReservationForm
from BarberBook.reservation.models import Reservation

UserModel = get_user_model()


def select_barbershop(request, slug):
    client = request.user
    barbershop = BarbershopProfile.objects.get(slug=slug)
    request.session['client_id'] = client.pk
    request.session['barbershop_slug'] = slug
    print(request.session['client_id'])
    print(request.session['barbershop_slug'])
    context = {
        'client': client,
        'barbershop': barbershop
    }
    return render(request, 'reservation/step1-select-barbershop.html', context)


def select_barbershop_service(request):
    client = UserModel.objects.get(pk=request.session['client_id'])
    barbershop = BarbershopProfile.objects.get(slug=request.session['barbershop_slug'])
    services = barbershop.barbershopservice_set.all()

    if request.method == 'POST':
        form = BarbershopServiceForm(request.POST, services=services)
        if form.is_valid():
            request.session['service_id'] = form.cleaned_data['service'].id
            return redirect('step3-select-barber')

    else:
        form = BarbershopServiceForm(services=services)

    context = {
        'client': client,
        'barbershop': barbershop,
        'form': form
    }
    return render(request, 'reservation/step2-select-barbershop-service.html', context)


def select_barber(request):
    client = UserModel.objects.get(pk=request.session['client_id'])
    barbershop = BarbershopProfile.objects.get(slug=request.session['barbershop_slug'])
    service = BarbershopService.objects.get(id=request.session['service_id'])
    barbers = barbershop.barber_set.all()
    if request.method == 'POST':
        form = BarbershopBarberForm(request.POST, barbers=barbers)
        if form.is_valid():
            request.session['barber_id'] = form.cleaned_data['barber'].id
            return redirect('step4-select-date')

    else:
        form = BarbershopBarberForm(barbers=barbers)

    context = {
        'client': client,
        'barbershop': barbershop,
        'service': service,
        'form': form
    }
    return render(request, 'reservation/step3-select-barber.html', context)


def select_date(request):
    client = UserModel.objects.get(pk=request.session['client_id'])
    barbershop = BarbershopProfile.objects.get(slug=request.session['barbershop_slug'])
    service = BarbershopService.objects.get(id=request.session['service_id'])
    barber = Barber.objects.get(id=request.session['barber_id'])

    if request.method == 'POST':
        form = DateSelectionForm(request.POST)
        if form.is_valid():
            request.session['date'] = form.cleaned_data['date'].isoformat()
            return redirect('step5-select-time')
    else:
        form = DateSelectionForm()

    context = {
        'client': client,
        'barbershop': barbershop,
        'service': service,
        'barber': barber,
        'form': form
    }
    return render(request, 'reservation/step4-select-date.html', context)


def select_time(request):
    client = UserModel.objects.get(pk=request.session['client_id'])
    barbershop = BarbershopProfile.objects.get(slug=request.session['barbershop_slug'])
    service = BarbershopService.objects.get(id=request.session['service_id'])
    barber = Barber.objects.get(id=request.session['barber_id'])
    reservation_date_str = request.session['date']
    reservation_date = datetime.strptime(reservation_date_str, '%Y-%m-%d').date()
    weekday_index = reservation_date.weekday()
    working_hours = barbershop.barbershopworkinghours_set.get(day=weekday_index)
    start_time = working_hours.start_time
    end_time = working_hours.end_time

    existing_reservations = Reservation.objects.filter(
        barbershop=barbershop,
        barber=barber,
        date=reservation_date
    )

    available_time_slots = []
    current_time = datetime.combine(reservation_date, start_time)
    end_datetime = datetime.combine(reservation_date, end_time)
    current_time = datetime.now() if current_time < datetime.now() else current_time

    if current_time.minute == 0:
        pass
    elif current_time.minute >= 30:
        current_time = current_time.replace(minute=0, second=0) + timedelta(hours=1)
    else:
        current_time = current_time.replace(minute=30, second=0)

    while current_time < end_datetime:
        time_slot = current_time.time()
        if not existing_reservations.filter(time=time_slot):
            available_time_slots.append((time_slot, time_slot.strftime('%H:%M')))
        current_time += timedelta(minutes=30)

    if request.method == 'POST':
        form = TimeSelectionForm(request.POST, choices=available_time_slots)
        if form.is_valid():
            reservation_time = form.cleaned_data['time_slot']
            request.session['reservation_time'] = reservation_time
        return redirect('create-reservation')
    else:
        form = TimeSelectionForm(choices=available_time_slots)

    context = {
        'client': client,
        'barbershop': barbershop,
        'service': service,
        'barber': barber,
        'reservation_date': reservation_date,
        'start_time': start_time,
        'end_time': end_time,
        'existing_reservations': existing_reservations,
        'form': form
    }
    return render(request, 'reservation/step5-select-time.html', context)


def create_reservation(request):
    client = UserModel.objects.get(pk=request.session['client_id'])
    barbershop = BarbershopProfile.objects.get(slug=request.session['barbershop_slug'])
    service = BarbershopService.objects.get(id=request.session['service_id'])
    barber = Barber.objects.get(id=request.session['barber_id'])
    reservation_date_str = request.session['date']
    reservation_date = datetime.strptime(reservation_date_str, '%Y-%m-%d').date()
    reservation_time_str = request.session['reservation_time']
    reservation_time = datetime.strptime(reservation_time_str, '%H:%M:%S').time()

    initial_data = {
        'client': client,
        'barbershop': barbershop,
        'service': service,
        'barber': barber,
        'date': reservation_date,
        'time': reservation_time,
    }

    if request.method == 'POST':
        form = ReservationForm(request.POST, initial=initial_data)
        if form.is_valid():
            form.save()
            del request.session['client_id']
            del request.session['barbershop_slug']
            del request.session['service_id']
            del request.session['barber_id']
            del request.session['date']
            del request.session['reservation_time']
            return redirect('home-page')
    else:
        form = ReservationForm(initial=initial_data)

    context = {
        'client': client,
        'barbershop': barbershop,
        'service': service,
        'barber': barber,
        'reservation_date': reservation_date,
        'reservation_time': reservation_time,
        'form': form
    }

    return render(request, 'reservation/create-reservation.html', context)