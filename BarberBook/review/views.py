from datetime import datetime

from django.contrib.auth import mixins as auth_mixins
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import generic as views
from django.shortcuts import render, redirect, get_object_or_404

from .forms import ReviewForm
from .models import Review


from ..barbershop.models import BarbershopProfile
from ..client.models import ClientProfile
from ..reservation.models import Reservation


@login_required
def create_review(request, slug):
    barbershop = BarbershopProfile.objects.get(slug=slug)
    user = request.user
    user_is_client = hasattr(user, 'clientprofile')
    has_reserved = Reservation.objects.filter(user=user, barbershop=barbershop, date__lte=datetime.today(), time__lt=datetime.now()).exists()
    has_reviewed = Review.objects.filter(user=user, barbershop=barbershop).exists()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.barbershop = barbershop
            review.save()
            return redirect('barbershop-details', slug=barbershop.slug)
        else:
            print(form.errors)
    else:
        form = ReviewForm()

    context = {
        'user_is_client': user_is_client,
        'has_reserved': has_reserved,
        'has_reviewed': has_reviewed,
        'barbershop': barbershop,
        'form': form,
    }

    return render(request, 'review/create-review.html', context)


class BarbershopReviewsListView(views.ListView):
    model = Review
    template_name = 'review/barbershop-reviews-list.html'
    context_object_name = 'reviews'
    paginate_by = 2

    def get_queryset(self):
        barbershop = get_object_or_404(BarbershopProfile, slug=self.kwargs['slug'])
        queryset = Review.objects.filter(barbershop=barbershop).order_by('-date_created')

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        barbershop = get_object_or_404(BarbershopProfile, slug=self.kwargs['slug'])
        context['barbershop'] = barbershop

        return context


class ClientReviewsListView(auth_mixins.LoginRequiredMixin, views.ListView):
    model = Review
    template_name = 'review/client-reviews-list.html'
    context_object_name = 'reviews'
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(ClientProfile, pk=self.kwargs['pk'])
        queryset = Review.objects.filter(user=user.pk).order_by('-date_created')

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = get_object_or_404(ClientProfile, pk=self.kwargs['pk'])
        context['user'] = user

        return context


class EditReviewView(auth_mixins.LoginRequiredMixin, views.UpdateView):
    model = Review
    template_name = 'review/edit-review.html'
    fields = ['rating', 'comment']
    success_url = reverse_lazy('client-details')

    def get_queryset(self):
        return Review.objects.filter(user=self.request.user)


class DeleteReviewView(auth_mixins.LoginRequiredMixin, views.DeleteView):
    model = Review
    template_name = 'review/delete-review.html'
    success_url = reverse_lazy('client-details')

    def get_queryset(self):
        return Review.objects.filter(user=self.request.user)
