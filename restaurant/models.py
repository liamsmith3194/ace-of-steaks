# from django.db import models
# from django.contrib.auth.models import User
# from cloudinary.models import CloudinaryField


# class Booking(models.Model):
#     booking_id = models.CharField('Booking ID', max_length=50, unique=True)
#     booking_date = models.DateTimeField('Date')
#     booking_fname = models.CharField('First Name', max_length=50)
#     booking_lname = models.CharField('Last Name', max_length=50)
#     booking_email = models.EmailField('Email')
#     booking_mobile = models.CharField('Contact No', max_length=50)
#     booking_location = models.CharField('Restuarant Location', max_length=50)
#     booking_quantity = models.CharField('Quantity', max_length=50)

#     class Meta:
#         ordering = ["-booking_date"]

#     def __str__(self):
#         return self.booking_id