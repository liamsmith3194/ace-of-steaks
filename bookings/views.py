from django.shortcuts import render
from . models import Booking

# Create your views here.

def manage_bookings(request):
    bookings = Booking.objects.all()
    page_title = 'Sport'
    return render(request,'bookings/manage-bookings.html', { 'bookings':bookings })

def book_table(request):
    return render(request, 'bookings/book.html')