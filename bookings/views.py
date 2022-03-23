from django.shortcuts import render, redirect
from django.http import HttpResponse
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


def admin_manage_booking(request):
    bookings = Booking.objects.all()
    return render(request, 'bookings/admin-manage-bookings.html',
                  {'bookings': bookings})


def manage_booking(request):
    booking_count = Booking.objects.filter(username=request.user).count()
    bookings = Booking.objects.filter(username=request.user)

    return render(request, 'bookings/manage-bookings.html',
                  {'bookings': bookings,
                   'booking_count': booking_count})


# def manage_booking(request):
#     booking_count = Booking.objects.filter(username=request.user).count()
#     bookings = Booking.objects.filter(username=request.user)
    
#     if Booking.objects.filter(id=request.user.id).exists():
#         return HttpResponse('booking exists')
#         # return render(request, 'bookings/manage-bookings.html')
#     else:
#         return render(request, 'menu.html')


# def restrict_booking(request):
#     restrict_booking = Booking.objects.filter(username=request.user).count()
#     return render(request, 'bookings/book.html',
#     {'bookings': restrict_booking})


def test_func(self):
    yesterday = datetime.now() - timedelta(day=1)
    # print to see which time is correct.
    print('this is yesterday...', yesterday)
    print('this is timezone.now()...', timezone.now())
    print('this is daytime.now()...', datetime.now())
    if Post.objects.filter(poster=self.request.user, post_date__gt=yesterday).exists():
        raise PermissionDenied("You have made your post today, Please come back later")
        return False
    else:
        return True




def restrict(self, request):
    if Booking.objects.filter(id=request.user.id).exists():
        return HttpResponse('booking exists')
        # return render(request, 'bookings/manage-bookings.html')
    else:
        return HttpResponse('booking DOESNT exists')

        # return render(request, 'menu.html')


# class PostLike(View):

#     def post(self, request, slug, *args, **kwargs):
#         post = get_object_or_404(Post, slug=slug)
#         if post.likes.filter(id=request.user.id).exists():
#             post.likes.remove(request.user)
#         else:
#             post.likes.add(request.user)

#         return HttpResponseRedirect(reverse('post_detail', args=[slug]))


# is this needed?
# def form_valid(self, form):
#     form.instance.poster = self.request.user
#     return super(AddPostView, self).form_valid(form)


# def remove_old_booking(request):


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
