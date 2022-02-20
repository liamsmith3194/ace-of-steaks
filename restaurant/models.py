from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Bookings(models.Model):
    booking_id = models.CharField(max_length=50, unique=True)
    booking_date = models.DateTimeField(auto_now_add=True)
    booking_fname = models.ForeignKey
    booking_lname = models.ForeignKey
    booking_email = models.EmailField
    booking_mobile = models.IntegerField
    booking_location = models.CharField(max_length=50)
    booking_quantity = models.CharField(max_length=50)

    class Meta:
        ordering = ["-booking_date"]

    def __str__(self):
        return self.booking_id