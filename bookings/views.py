from django.shortcuts import render, redirect
from .models import Booking
from .forms import BookingForm, DateTimeInput
from django.utils import timezone

# Create your views here.


def make_booking(request):
    booking_count = Booking.objects.filter(
        username=request.user, date__gte=timezone.now()).count()
    form = BookingForm
    if request.method == 'POST':
        # print('Printing POST:', request.POST)
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/bookings/manage/')
        else:
            print(form.errors.as_data())  # here you print errors to terminal
    return render(request, 'bookings/book.html', {'form': form, 'booking_count': booking_count})


def manage_booking(request):
    booking_count = Booking.objects.filter(
        username=request.user, date__gte=timezone.now()).count()
    bookings = Booking.objects.filter(
        username=request.user, date__gte=timezone.now())

    return render(request, 'bookings/manage-booking.html',
                  {'bookings': bookings,
                   'booking_count': booking_count})


def update_booking(request, pk):
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
    booking = Booking.objects.get(id=pk)
    if request.method == 'POST':
        booking.delete()
        return redirect('/bookings/manage/')

    context = {'booking': booking}
    return render(request, 'bookings/delete-booking.html', context)
