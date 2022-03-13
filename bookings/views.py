from django.shortcuts import render, redirect
from .models import Booking
from .forms import BookingForm

# Create your views here.

def ManageBookings(request):
    bookings = Booking.objects.all()
    return render(request,'bookings/manage-bookings.html', { 'bookings':bookings })


def BookTable(request):

    form = BookingForm
    if request.method == 'POST':
        # print('Printing POST:', request.POST)
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/bookings/manage/')


    context = {'form':form}
    return render(request, 'bookings/book.html', context)
