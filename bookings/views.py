from django.shortcuts import render, redirect
from .models import Booking
from .forms import BookingForm

# Create your views here.


def make_booking(request):

    form = BookingForm
    if request.method == 'POST':
        # print('Printing POST:', request.POST)
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/bookings/manage/')

    context = {'form': form}
    return render(request, 'bookings/book.html', context)

    # bookings = Booking.objects.filter(username='6')
    # user_posts=Post.objects.filter(user=request.user)
    # user_posts=Post.objects.filter(user_id=pk)



# def manage_booking(request):
#     bookings = Booking.objects.filter(username='6')
#     return render(request, 'bookings/manage-bookings.html',
#     {'bookings': bookings})

# def manage_booking(request):
#     bookings = Booking.objects.all()
#     return render(request, 'bookings/manage-bookings.html',
#     {'bookings': bookings})

def manage_booking(request):
    bookings = Booking.objects.filter(username=request.user)
    return render(request, 'bookings/manage-bookings.html',
    {'bookings': bookings})


def update_booking(request, pk):
    booking = Booking.objects.get(id=pk)
    form = BookingForm(instance=booking)

    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('/bookings/manage/')

    context = {'form': form}
    return render(request, 'bookings/book.html', context)


def delete_booking(request, pk):
    booking = Booking.objects.get(id=pk)
    if request.method == 'POST':
        booking.delete()
        return redirect('/bookings/manage/')

    context = {'booking': booking}
    return render(request, 'bookings/delete-booking.html', context)
