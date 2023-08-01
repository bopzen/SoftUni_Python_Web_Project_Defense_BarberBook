from django.db.models import Avg
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import mixins as auth_mixins
from django.views import generic as views


from BarberBook.barbershop.models import BarbershopProfile, BarbershopService, BarbershopWorkingHours, BarbershopPicture
from BarberBook.review.models import Review


class EditBarbershopProfileView(auth_mixins.LoginRequiredMixin, views.UpdateView):
    model = BarbershopProfile
    template_name = 'barbershop/edit-barbershop.html'
    fields = ['name', 'address', 'city', 'geolocation_latitude', 'geolocation_longitude', 'about', 'barbershop_picture']

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        barbershop_rating = Review.objects.filter(barbershop=self.object.pk).aggregate(Avg('rating'))['rating__avg']
        barbershop_reviews_count = Review.objects.filter(barbershop=self.object.pk).count()
        context['barbershop_rating'] = barbershop_rating
        context['barbershop_reviews_count'] = barbershop_reviews_count
        return context


class BarbershopListView(views.ListView):
    model = BarbershopProfile
    template_name = 'barbershop/barbershops-list.html'
    context_object_name = 'barbershops'
    paginate_by = 6


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


class BarbershopWorkingHoursDetailsView(auth_mixins.LoginRequiredMixin, auth_mixins.UserPassesTestMixin, views.DetailView):
    model = BarbershopWorkingHours
    template_name = 'barbershop/working-hours-details.html'

    def test_func(self):
        barber = self.get_object()
        return barber.barbershop.user == self.request.user


class EditBarbershopWorkingHoursView(auth_mixins.LoginRequiredMixin, auth_mixins.UserPassesTestMixin, views.UpdateView):
    model = BarbershopWorkingHours
    template_name = 'barbershop/edit-working-hours.html'
    fields = ['start_time', 'end_time']

    def get_success_url(self):
        barbershop = BarbershopProfile.objects.get(user=self.request.user)
        return reverse_lazy('barbershop-details', kwargs={'slug': barbershop.slug})

    def test_func(self):
        barber = self.get_object()
        return barber.barbershop.user == self.request.user


class CreateBarbershopPictureView(auth_mixins.LoginRequiredMixin, views.CreateView):
    model = BarbershopPicture
    template_name = 'pictures/create-picture.html'
    fields = ['image']

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


class DeleteBarbershopPictureView(auth_mixins.LoginRequiredMixin, auth_mixins.UserPassesTestMixin, views.DeleteView):
    model = BarbershopPicture
    template_name = 'pictures/delete-picture.html'

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


class BarbershopPictureDetailsView(views.DetailView):
    model = BarbershopPicture
    template_name = 'pictures/picture-details.html'
