from django.shortcuts import render, redirect
from .models import Booking
from .forms import BookingForm, DateTimeInput
from datetime import datetime




# Create your views here.



# def duplicate(self):
#     for instance in Booking.objects.all():
#         if instance.fname == fname:
#             raise forms.ValidationError(str(fname) + 'is already created')
#             return redirect('/menu/')
#             print('this is yesterday...')

# def test2(request):
#     Booking.objects.filter(fname).exists()
# print('working')

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


def manage_booking(request):
    booking_count = Booking.objects.filter(username=request.user).count()
    bookings = Booking.objects.filter(username=request.user)

    return render(request, 'bookings/manage-bookings.html',
                  {'bookings': bookings,
                   'booking_count': booking_count})


# def remove_old_booking(request):
#     start_date=datetime(2009, 12, 30)
#     end_date=datetime(2020,12,30)
#     Booking().objects.filter(date__range=[start_date,end_date])
#     return render(request, 'bookings/manage-bookings.html')


# def test_func(self):
#     yesterday = datetime.now() - timedelta(day=1)
#     # print to see which time is correct.
#     print('this is yesterday...', yesterday)
#     print('this is timezone.now()...', timezone.now())
#     print('this is daytime.now()...', datetime.now())
#     if Post.objects.filter(poster=self.request.user, post_date__gt=yesterday).exists():
#         raise PermissionDenied("You have made your post today, Please come back later")
#         return False
#     else:
#         return True


# def restrict(self, request):
#     if Booking.objects.filter(id=request.user.id).exists():
#         return HttpResponse('booking exists')
#         return render(request, 'bookings/manage-bookings.html')
#     else:
#         return HttpResponse('booking DOESNT exists')


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
    return render(request, 'bookings/book.html', context)


def delete_booking(request, pk):
    booking = Booking.objects.get(id=pk)
    if request.method == 'POST':
        booking.delete()
        return redirect('/bookings/manage/')

    context = {'booking': booking}
    return render(request, 'bookings/delete-booking.html', context)
