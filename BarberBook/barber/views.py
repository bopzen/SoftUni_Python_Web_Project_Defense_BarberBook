from django.shortcuts import render
from django.contrib.auth import mixins as auth_mixins
from django.urls import reverse_lazy
from django.views import generic as views

from BarberBook.barber.models import Barber


class CreateBarberView(auth_mixins.LoginRequiredMixin, views.CreateView):
    model = Barber
    template_name = 'barber/create-barber.html'
    fields = ['name', 'about']
    success_url = reverse_lazy('barbershop-details')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# def add_barber(request):
#     return render(request, 'barber/create-barber.html')


def edit_barber(request):
    return render(request, 'barber/edit-barber.html')


def delete_barber(request):
    return render(request, 'barber/delete-barber.html')


def barber_details(request):
    return render(request, 'barber/barber-details.html')


def barbers_list(request):
    return render(request, 'barber/barbers-list.html')