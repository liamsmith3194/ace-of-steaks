from django.contrib import admin
from .models import Booking

# admin.site.register(Booking)

@admin.register(Booking)

class BookingAdmin(admin.ModelAdmin):
    prepopulated_fields = {'booking_id': ('booking_lname',)}
    list_filter = ('booking_lname', 'booking_date')
