from .models import Booking
from django import forms
from django.forms import ModelForm
import datetime

class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking

        # fields = '__all__'
        fields = ['username', 'date', 'fname', 'lname', 'email', 'location', 'quantity']
        widgets = {
            'username': forms.TextInput(attrs={'value': '', 'id': 'user_id', 'type': 'hidden'}),
            'date': DateTimeInput(
                {
                    'minDate': (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%Y-%m-%d 00:00:00'),
                    'maxDate': (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%Y-%m-%d 23:59:59'),
                    'enabledHours': [8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
                }
                ),
            }
    
    def clean_fname(self):
        fname = self.cleaned_data.get('fname')
        if (fname == ""):
            raise forms.ValidationError("blank")
        
        for instance in Booking.objects.all():
            if instance.fname == fname:
                raise forms.ValidationError("exists")
        return fname