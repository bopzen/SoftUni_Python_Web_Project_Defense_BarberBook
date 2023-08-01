from django.urls import path

from BarberBook.common.views import home_page, map_page, search_view

urlpatterns = [
    path('', home_page, name='home-page'),
    path('map-all-barbershops', map_page, name='map-page'),
    path('search/', search_view, name='search-view')
]