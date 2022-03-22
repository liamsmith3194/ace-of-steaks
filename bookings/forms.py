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
            'date': DateTimeInput(attrs={'min': '08.00', 'max': '17.00'}),
            'username': forms.TextInput(attrs={'value': '', 'id': 'user_id', 'type': 'hidden'})
        }

            # options={
            #         'enabledHours': [8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
            #     }
            # ),