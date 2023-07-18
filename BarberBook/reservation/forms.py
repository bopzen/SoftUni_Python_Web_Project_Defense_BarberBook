import datetime

from django import forms
from django.db.models import Q
from django.utils import timezone
from django.utils.safestring import mark_safe
from datetime import date, timedelta

from .models import Reservation
from ..barber.models import Barber
from ..barbershop.models import BarbershopService


class BarbershopServiceForm(forms.Form):
    service = forms.ModelChoiceField(queryset=None)

    def __init__(self, *args, **kwargs):
        services = kwargs.pop('services')
        super().__init__(*args, **kwargs)
        self.fields['service'].queryset = services


class BarbershopBarberForm(forms.Form):
    barber = forms.ModelChoiceField(queryset=None)

    def __init__(self, *args, **kwargs):
        barbers = kwargs.pop('barbers')
        super().__init__(*args, **kwargs)
        self.fields['barber'].queryset = barbers


class DateSelectionForm(forms.Form):
    date = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control datepicker', 'autocomplete': 'off'}),
        label='Select Date'
    )


class TimeSelectionForm(forms.Form):
    time_slot = forms.ChoiceField(label='Select Time Slot', choices=())

    def __init__(self, *args, **kwargs):
        time_slot_choices = kwargs.pop('choices', ())
        super().__init__(*args, **kwargs)  # Update this line
        self.fields['time_slot'].choices = time_slot_choices


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('client', 'barbershop', 'service', 'barber', 'date', 'time')
        widgets = {
            'client': forms.HiddenInput(),
            'barbershop': forms.HiddenInput(),
            'service': forms.HiddenInput(),
            'barber': forms.HiddenInput(),
            'date': forms.HiddenInput(),
            'time': forms.HiddenInput(),
        }

