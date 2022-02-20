from django.contrib import admin
from .models import Booking

# admin.site.register(Booking)

@admin.register(Booking)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('booking_id', 'booking_date', 'booking_lname', 'booking_location', 'booking_quantity' )
    prepopulated_fields = {'booking_id': ('booking_lname',)}
    list_filter = ('booking_location', 'booking_date')
    search_fields = ['booking_fname', 'booking_lname']
