from .models import Booking
from django import forms
from django.forms import ModelForm

class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking

        # fields = '__all__'
        fields = ['username', 'date', 'fname', 'lname', 'email', 'location', 'quantity']
        widgets = {
            'date': DateTimeInput()
        }