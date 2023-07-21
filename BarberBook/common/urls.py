from django.urls import path

from BarberBook.common.views import home_page, map_page

urlpatterns = [
    path('', home_page, name='home-page'),
    path('map-all-barbershops', map_page, name='map-page')
]