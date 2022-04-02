from .models import Booking
from django import forms
from django.forms import ModelForm
import datetime


class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'


today = datetime.datetime.today()
min_date = (today + datetime.timedelta(days=1)).strftime("%Y-%m-%dT08:00:00")
max_date = (today + datetime.timedelta(days=30)).strftime("%Y-%m-%dT22:00:00")


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['username', 'date', 'fname',
                  'lname', 'email', 'location', 'quantity']
        widgets = {
            'username': forms.TextInput(attrs={'value': '', 'id': 'user_id'}),
            # , 'type': 'hidden'
            'email': forms.EmailInput(attrs={'value': '', 'id': 'user_email'}),

            'date': DateTimeInput(
                attrs={
                    "id": "date_id",
                    "value": min_date,
                    "min": min_date,
                    "max": max_date,
                }
            ),
        }

    def clean_date(self):
        date = self.cleaned_data.get('date')
        if (date == ""):
            raise forms.ValidationError("This field can not be left blank")

        for instance in Booking.objects.all():
            if instance.date == date:
                raise forms.ValidationError(
                    "Date and/or time not available, please try again.")
        return date
