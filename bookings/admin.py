from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = ('id', 'username', 'date', 'fname', 'lname', 'location', 'quantity')
    list_filter = ('location', 'date')
    search_fields = ['fname', 'lname']
