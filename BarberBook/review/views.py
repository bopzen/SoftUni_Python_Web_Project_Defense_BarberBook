from datetime import datetime

from django.contrib.auth import mixins as auth_mixins
from django.contrib.auth.decorators import login_required
from django.views import generic as views
from django.shortcuts import render, redirect, get_object_or_404

from .forms import ReviewForm
from .models import Review


from ..barbershop.models import BarbershopProfile
from ..reservation.models import Reservation


@login_required
def create_review(request, slug):
    barbershop = BarbershopProfile.objects.get(slug=slug)
    user = request.user
    user_is_client = hasattr(user, 'clientprofile')
    has_reserved = Reservation.objects.filter(user=user, barbershop=barbershop, date__lt=datetime.today()).exists()
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