from django.http import HttpResponse
from django.shortcuts import render
# from django.views import generic, View
# from .models import Booking

# class IndexPage(generic.ListView):
#     template_name = 'index.html'



# class BookingList(generic.ListView):
#     model = Booking
#     queryset = Booking.objects.order_by('-booking_date')
#     template_name = 'bookings.html'
#     paginate_by = 20


def index(request):
    return render(request, 'index.html')

def menu(request):
    return render(request, 'menu.html')
