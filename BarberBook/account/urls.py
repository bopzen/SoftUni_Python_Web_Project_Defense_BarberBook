from django.urls import path

from BarberBook.account.views import UserRegisterView, UserLoginView, UserLogoutView, UserDeleteView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register-page'),
    path('login/', UserLoginView.as_view(), name='login-page'),
    path('delete/', UserDeleteView.as_view(), name='delete-account'),
    path('logout/', UserLogoutView.as_view(), name='logout-page')
]