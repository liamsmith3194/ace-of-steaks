from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from cloudinary.models import CloudinaryField


LOCATIONS = [('London', 'London'), ('Glasgow', 'Glasgow'), ('Cardiff', 'Cardiff')]

NUMBER_OF_GUESTS = [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')]

class Booking(models.Model):
    date = models.DateTimeField()
    username = models.ForeignKey(User, on_delete=models.CASCADE, default=None,)
    fname = models.CharField('First Name', max_length=50)
    lname = models.CharField('Last Name', max_length=50)
    email = models.EmailField('Email')
    location = models.CharField('Restuarant Location', max_length=50, choices=LOCATIONS,)
    quantity = models.CharField('Number of Guests', max_length=50, choices=NUMBER_OF_GUESTS,)

    # prepopulated_fields = {'reference': ('fname', 'lname','location')}

    class Meta:
        ordering = ["-date"]

    # def __str__(self):
    #     return self.id
