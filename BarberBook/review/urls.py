from django.urls import path

from BarberBook.review.views import create_review

urlpatterns = [
    path('create-review/<slug:slug>/', create_review, name='create-review'),
]