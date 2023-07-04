from django.urls import path

from BarberBook.common.views import home_page, register_page, login_page, logout_page, profile_page

urlpatterns = [
    path('', home_page, name='home-page'),
    path('register/', register_page, name='register-page'),
    path('login/', login_page, name='login-page'),
    path('logout/', logout_page, name='logout-page'),
    path('profile/', profile_page, name='profile-page')
]