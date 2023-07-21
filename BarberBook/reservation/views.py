from datetime import datetime, timedelta
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse

from BarberBook.barber.models import Barber
from BarberBook.barbershop.models import BarbershopProfile, BarbershopService
from BarberBook.reservation.forms import BarbershopServiceForm, BarbershopBarberForm, DateSelectionForm, \
    TimeSelectionForm, ReservationForm
from BarberBook.reservation.models import Reservation
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins

UserModel = get_user_model()


@login_required
def select_barbershop(request, slug):
    user = request.user
    barbershop = BarbershopProfile.objects.get(slug=slug)
    request.session['user_id'] = user.pk
    request.session['barbershop_slug'] = slug
    print(request.session['user_id'])
    print(request.session['barbershop_slug'])
    context = {
        'user': user,
        'barbershop': barbershop
    }
    return render(request, 'reservation/step1-select-barbershop.html', context)


@login_required
def select_barbershop_service(request):
    user = UserModel.objects.get(pk=request.session['user_id'])
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
        'user': user,
        'barbershop': barbershop,
        'form': form
    }
    return render(request, 'reservation/step2-select-barbershop-service.html', context)


@login_required
def select_barber(request):
    user = UserModel.objects.get(pk=request.session['user_id'])
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
        'user': user,
        'barbershop': barbershop,
        'service': service,
        'form': form
    }
    return render(request, 'reservation/step3-select-barber.html', context)


@login_required
def select_date(request):
    user = UserModel.objects.get(pk=request.session['user_id'])
    barbershop = BarbershopProfile.objects.get(slug=request.session['barbershop_slug'])
    service = BarbershopService.objects.get(id=request.session['service_id'])
    barber = Barber.objects.get(id=request.session['barber_id'])

    if request.method == 'POST':
        form = DateSelectionForm(request.POST)
        if form.is_valid():
            reservation_date = form.cleaned_data['date']
            weekday_index = reservation_date.weekday()
            working_hours = barbershop.barbershopworkinghours_set.filter(day=weekday_index).first()
            start_time = working_hours.start_time
            end_time = working_hours.end_time
            if start_time is None and end_time is None:
                form.add_error('date', 'This day is not available for reservations.')
            else:
                request.session['date'] = form.cleaned_data['date'].isoformat()
                return redirect('step5-select-time')
    else:
        form = DateSelectionForm()

    context = {
        'user': user,
        'barbershop': barbershop,
        'service': service,
        'barber': barber,
        'form': form
    }
    return render(request, 'reservation/step4-select-date.html', context)


@login_required
def select_time(request):
    user = UserModel.objects.get(pk=request.session['user_id'])
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
    print(current_time)
    current_time = datetime.now() if current_time < datetime.now() else current_time
    print(current_time)

    if current_time.minute == 0:
        current_time = current_time.replace(minute=0, second=0, microsecond=0)
    elif current_time.minute >= 30:
        current_time = current_time.replace(minute=0, second=0, microsecond=0) + timedelta(hours=1)
    else:
        current_time = current_time.replace(minute=30, second=0, microsecond=0)

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
        'user': user,
        'barbershop': barbershop,
        'service': service,
        'barber': barber,
        'reservation_date': reservation_date,
        'form': form
    }
    return render(request, 'reservation/step5-select-time.html', context)


@login_required
def create_reservation(request):
    user = UserModel.objects.get(pk=request.session['user_id'])
    barbershop = BarbershopProfile.objects.get(slug=request.session['barbershop_slug'])
    service = BarbershopService.objects.get(id=request.session['service_id'])
    barber = Barber.objects.get(id=request.session['barber_id'])
    reservation_date_str = request.session['date']
    reservation_date = datetime.strptime(reservation_date_str, '%Y-%m-%d').date()
    reservation_time_str = request.session['reservation_time']
    reservation_time = datetime.strptime(reservation_time_str, '%H:%M:%S').time()

    initial_data = {
        'user': user,
        'barbershop': barbershop,
        'service': service,
        'barber': barber,
        'date': reservation_date,
        'time': reservation_time,
    }

    if request.method == 'POST':
        form = ReservationForm(request.POST, initial=initial_data)
        if form.is_valid():
            reservation = form.save()
            request.session['reservation_id'] = reservation.id
            return redirect('reservation-success')
    else:
        form = ReservationForm(initial=initial_data)

    context = {
        'user': user,
        'barbershop': barbershop,
        'service': service,
        'barber': barber,
        'reservation_date': reservation_date,
        'reservation_time': reservation_time,
        'form': form
    }

    return render(request, 'reservation/create-reservation.html', context)


@login_required()
def reservation_success(request):
    reservation = Reservation.objects.get(pk=request.session['reservation_id'])
    user = UserModel.objects.get(pk=request.session['user_id'])
    barbershop = BarbershopProfile.objects.get(slug=request.session['barbershop_slug'])
    service = BarbershopService.objects.get(id=request.session['service_id'])
    barber = Barber.objects.get(id=request.session['barber_id'])
    reservation_date_str = request.session['date']
    reservation_date = datetime.strptime(reservation_date_str, '%Y-%m-%d').date()
    reservation_time_str = request.session['reservation_time']
    reservation_time = datetime.strptime(reservation_time_str, '%H:%M:%S').time()

    del request.session['reservation_id']
    del request.session['user_id']
    del request.session['barbershop_slug']
    del request.session['service_id']
    del request.session['barber_id']
    del request.session['date']
    del request.session['reservation_time']

    context = {
        'reservation': reservation,
        'user': user,
        'barbershop': barbershop,
        'service': service,
        'barber': barber,
        'reservation_date': reservation_date,
        'reservation_time': reservation_time,
    }

    return render(request, 'reservation/reservation-success.html', context)


class ReservationsListView(auth_mixins.LoginRequiredMixin, views.ListView):
    model = Reservation
    template_name = 'reservation/reservations-list.html'
    context_object_name = 'reservations'
    paginate_by = 3

    def get_queryset(self):
        user = self.request.user

        if user.is_authenticated:
            if hasattr(user, 'clientprofile'):
                queryset = Reservation.objects.filter(user=user.id)
            elif hasattr(user, 'barbershopprofile'):
                queryset = Reservation.objects.filter(barbershop=user.barbershopprofile)
            else:
                queryset = Reservation.objects.none()
        else:
            queryset = Reservation.objects.none()

        user_filter = self.request.GET.get('user_filter', None)
        if user_filter:
            queryset = queryset.filter(Q(user__username__icontains=user_filter))

        date_filter = self.request.GET.get('date_filter')
        if date_filter:
            queryset = queryset.filter(date=date_filter)

        barber_filter = self.request.GET.get('barber_filter')
        if barber_filter:
            queryset = queryset.filter(Q(barber__name__icontains=barber_filter))

        barbershop_filter = self.request.GET.get('barbershop_filter')
        if barbershop_filter:
            queryset = queryset.filter(Q(barbershop__name__icontains=barbershop_filter))

        return queryset


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_datetime = datetime.now()

        past_reservations = self.get_queryset().filter(
            Q(date__lt=current_datetime.date()) |
            Q(date=current_datetime.date(), time__lte=current_datetime.time())
        ).order_by('-date', '-time')

        upcoming_reservations = self.get_queryset().filter(
            Q(date__gt=current_datetime.date()) |
            Q(date=current_datetime.date(), time__gt=current_datetime.time())
        ).order_by('date', 'time')

        paginator_past = Paginator(past_reservations, self.paginate_by)
        page_number_past = self.request.GET.get('page_past')
        past_reservations_page = paginator_past.get_page(page_number_past)
        context['past_reservations'] = past_reservations_page

        paginator_upcoming = Paginator(upcoming_reservations, self.paginate_by)
        page_number_upcoming = self.request.GET.get('page_upcoming')
        upcoming_reservations_page = paginator_upcoming.get_page(page_number_upcoming)
        context['upcoming_reservations'] = upcoming_reservations_page

        return context


class DeleteReservationView(auth_mixins.LoginRequiredMixin, views.DeleteView):
    model = Reservation
    template_name = 'reservation/delete-reservation.html'

    def get_success_url(self):
        user = self.request.user
        return reverse_lazy('reservation-list', kwargs={'pk': user.pk})

    def test_func(self):
        reservation = self.get_object()
        return self.request.user == reservation.user or self.request.user == reservation.barbershop.user


