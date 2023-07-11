from django.urls import path

from BarberBook.common.views import home_page

urlpatterns = [
    path('', home_page, name='home-page')
]