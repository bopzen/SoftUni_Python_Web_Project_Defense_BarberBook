from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import mixins as auth_mixins
from django.views import generic as views

from BarberBook.barbershop.models import BarbershopProfile


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