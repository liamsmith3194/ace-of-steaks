from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Booking
from .forms import BookingForm, DateTimeInput


def make_booking(request):
    """Indentifies user by id and checks if user has an exisitng booking,
    if valid booking is saved and user is redirected to manage page"""
    booking_count = Booking.objects.filter(
        username=request.user, date__gte=timezone.now()).count()
    form = BookingForm
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/bookings/manage/')
    return render(request, 'bookings/book.html',
                  {'form': form, 'booking_count': booking_count})


def manage_booking(request):
    """Indentifies user by id and displays booking data providing
    the date has not passed"""
    booking_count = Booking.objects.filter(
        username=request.user, date__gte=timezone.now()).count()
    bookings = Booking.objects.filter(
        username=request.user, date__gte=timezone.now())
    return render(request, 'bookings/manage-booking.html',
                  {'bookings': bookings,
                   'booking_count': booking_count})


def update_booking(request, pk):
    """Returns the users booking data to the form, if
    the changes are a valid the form saves and updates the
    database returning the user to the manage page"""
    booking = Booking.objects.get(id=pk)
    form = BookingForm(instance=booking)
    date = DateTimeInput()
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('/bookings/manage/')
    context = {'form': form, 'date': date}
    return render(request, 'bookings/update-booking.html', context)


def delete_booking(request, pk):
    """Returns the users booking id, if user clicks delete
    the booking is removed from the database and redirects
    the user to the manage page"""
    booking = Booking.objects.get(id=pk)
    if request.method == 'POST':
        booking.delete()
        return redirect('/bookings/manage/')
    context = {'booking': booking}
    return render(request, 'bookings/delete-booking.html', context)
