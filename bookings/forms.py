import datetime
from django import forms
from allauth.account.forms import SignupForm
from .models import Booking

today = datetime.datetime.today()
min_date = (today + datetime.timedelta(days=1)).strftime("%Y-%m-%dT11:00:00")
max_date = (today + datetime.timedelta(days=30)).strftime("%Y-%m-%dT22:00:00")


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Enter your first name"}))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={"placeholder": "Enter your last name"}))


    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user


class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['username', 'date', 'fname',
                  'lname', 'email', 'location', 'quantity']
        widgets = {
            'username': forms.TextInput(attrs={'value': '', 'id': 'user_id',
                                               'type': 'hidden'}),
            'email': forms.EmailInput(attrs={'value': '', 'id': 'user_email'}),
            'fname': forms.TextInput(attrs={'value': '',
                                            'id': 'user_first_name'}),
            'lname': forms.TextInput(attrs={'value': '',
                                            'id': 'user_last_name'}),
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
