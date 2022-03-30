from .models import Booking
from django import forms
from django.forms import ModelForm
import datetime

class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking

        fields = ['username', 'date', 'fname', 'lname', 'email', 'location', 'quantity']
        widgets = {
            'username': forms.TextInput(attrs={'value': '', 'id': 'user_id'}),
            # , 'type': 'hidden'
            'email': forms.EmailInput(attrs={'value': '', 'id': 'user_email'}),

            'date': DateTimeInput(
                {
                    'minDate': (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%Y-%m-%d 00:00:00'),
                    'maxDate': (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%Y-%m-%d 23:59:59'),
                    'enabledHours': [8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
                }
                ),
            }
    
    def clean_date(self):
        date = self.cleaned_data.get('date')
        if (date == ""):
            raise forms.ValidationError("This field can not be left blank")
        
        for instance in Booking.objects.all():
            if instance.date == date:
                raise forms.ValidationError("Date and/or time not available, please try again.")
        return date