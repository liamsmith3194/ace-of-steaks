from . import views
from django.urls import path


urlpatterns = [
    path('', views.BookingList.as_view(), name='manage_booking'),
    path('manage_bookings.html', views.BookingList.as_view(), name='manage_booking'),
]