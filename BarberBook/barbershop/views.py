from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import mixins as auth_mixins
from django.views import generic as views

from BarberBook.barbershop.models import BarbershopProfile, BarbershopService


class EditBarbershopProfileView(auth_mixins.LoginRequiredMixin, views.UpdateView):
    model = BarbershopProfile
    template_name = 'barbershop/edit-barbershop.html'
    fields = ['name', 'address', 'city', 'about', 'barbershop_picture']

    def get_success_url(self):
        barbershop = BarbershopProfile.objects.get(user=self.request.user)
        return reverse_lazy('barbershop-details', kwargs={'slug': barbershop.slug})

    def get_object(self, queryset=None):
        return BarbershopProfile.objects.get(user_id=self.request.user)

    def form_valid(self, form):
        if self.request.user != self.get_object().user:
            return redirect('home-page')

        result = super().form_valid(form)

        return result


class BarbershopProfileDetailsView(views.DetailView):
    model = BarbershopProfile
    template_name = 'barbershop/barbershop-details.html'
    context_object_name = 'barbershop_profile'


def barbershop_list(request):
    return render(request, 'barbershop/barbershops-list.html')


class CreateBarbershopServiceView(auth_mixins.LoginRequiredMixin, views.CreateView):
    model = BarbershopService
    template_name = 'services/create-service.html'
    fields = ['category', 'service_name', 'price']

    def get_success_url(self):
        barbershop = BarbershopProfile.objects.get(user=self.request.user)
        return reverse_lazy('barbershop-details', kwargs={'slug': barbershop.slug})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        barbershop = BarbershopProfile.objects.get(user=self.request.user)
        context['barbershop'] = barbershop
        return context

    def form_valid(self, form):
        form.instance.barbershop = BarbershopProfile.objects.get(user=self.request.user)
        return super().form_valid(form)


class EditBarbershopServiceView(auth_mixins.LoginRequiredMixin, auth_mixins.UserPassesTestMixin, views.UpdateView):
    model = BarbershopService
    template_name = 'services/edit-service.html'
    fields = ['category', 'service_name', 'price']

    def get_success_url(self):
        barbershop = BarbershopProfile.objects.get(user=self.request.user)
        return reverse_lazy('service-details', kwargs={'pk': self.object.pk, 'slug': barbershop.slug})

    def test_func(self):
        barber = self.get_object()
        return barber.barbershop.user == self.request.user


class DeleteBarbershopServiceView(auth_mixins.LoginRequiredMixin, auth_mixins.UserPassesTestMixin, views.DeleteView):
    model = BarbershopService
    template_name = 'services/delete-service.html'

    def get_success_url(self):
        barbershop = BarbershopProfile.objects.get(user=self.request.user)
        return reverse_lazy('barbershop-details', kwargs={'slug': barbershop.slug})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        barbershop = BarbershopProfile.objects.get(user=self.request.user)
        context['barbershop'] = barbershop
        return context

    def test_func(self):
        barber = self.get_object()
        return barber.barbershop.user == self.request.user


class BarbershopServicesDetailsView(views.DetailView):
    model = BarbershopService
    template_name = 'services/service-details.html'
