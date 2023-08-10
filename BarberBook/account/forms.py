from django.contrib.auth import get_user_model
from django.contrib.auth import forms as auth_forms
from BarberBook.account.models import AppUser
from BarberBook.barbershop.models import BarbershopProfile
from BarberBook.client.models import ClientProfile
from django import forms

UserModel = get_user_model()


class RegisterUserForm(auth_forms.UserCreationForm):
    role = forms.ChoiceField(
        choices=AppUser.ROLES,
        widget=forms.RadioSelect,
        required=True,
        initial='Client'
    )

    class Meta(auth_forms.UserCreationForm.Meta):
        model = UserModel
        fields = ('username', 'email', 'role')

    def save(self, commit=True):
        user = super().save(commit)
        if user.role == 'Client':
            profile = ClientProfile(
                user=user
            )
        else:
            profile = BarbershopProfile(
                user=user
            )
        if commit:
            profile.save()
        return user
