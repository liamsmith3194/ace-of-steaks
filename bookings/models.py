from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

LOCATIONS = [('London', 'London'), ('Glasgow', 'Glasgow'), ('Cardiff', 'Cardiff')]

NUMBER_OF_GUESTS = [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')]

class Booking(models.Model):
    date = models.DateTimeField('Date')
    username = models.ForeignKey(User, on_delete=models.CASCADE, default=None,)
    fname = models.CharField('First Name', max_length=50)
    lname = models.CharField('Last Name', max_length=50)
    email = models.EmailField('Email', unique=True,)
    location = models.CharField('Restuarant Location', max_length=50, choices=LOCATIONS,)
    quantity = models.CharField('Number of Guests', max_length=50, choices=NUMBER_OF_GUESTS,)
    reference = models.CharField('Booking ID', max_length=50)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return self.reference