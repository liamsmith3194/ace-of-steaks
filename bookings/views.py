from django.shortcuts import render

# Create your views here.

def manage_bookings(request):
    return render(request, 'bookings/manage-bookings.html')