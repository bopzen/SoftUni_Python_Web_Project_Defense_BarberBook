from django.shortcuts import render, redirect
from django.contrib.auth import mixins as auth_mixins
from django.urls import reverse_lazy
from django.views import generic as views

from BarberBook.barber.models import Barber
from BarberBook.barbershop.models import BarbershopProfile


class CreateBarberView(auth_mixins.LoginRequiredMixin, views.CreateView):
    model = Barber
    template_name = 'barber/create-barber.html'
    fields = ['name', 'about', 'barber_picture']

    def get_success_url(self):
        barbershop = BarbershopProfile.objects.get(user=self.request.user)
        return reverse_lazy('barbershop-details', kwargs={'slug': barbershop.slug})

    def form_valid(self, form):
        form.instance.barbershop = BarbershopProfile.objects.get(user=self.request.user)
        return super().form_valid(form)


class EditBarberView(auth_mixins.LoginRequiredMixin, auth_mixins.UserPassesTestMixin, views.UpdateView):
    model = Barber
    template_name = 'barber/edit-barber.html'
    fields = ['name', 'about', 'barber_picture']

    def get_success_url(self):
        return reverse_lazy('barber-details', kwargs={'pk': self.object.pk})

    def test_func(self):
        barber = self.get_object()
        return barber.barbershop.user == self.request.user


class DeleteBarberView(auth_mixins.LoginRequiredMixin, auth_mixins.UserPassesTestMixin, views.DeleteView):
    model = Barber
    template_name = 'barber/delete-barber.html'

    def get_success_url(self):
        barbershop = BarbershopProfile.objects.get(user=self.request.user)
        return reverse_lazy('barbershop-details', kwargs={'slug': barbershop.slug})

    def test_func(self):
        barber = self.get_object()
        return barber.barbershop.user == self.request.user


class BarberDetailsView(views.DetailView):
    model = Barber
    template_name = 'barber/barber-details.html'


def barbers_list(request):
    return render(request, 'barber/barbers-list.html')