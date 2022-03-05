from . import views
from django.urls import path


urlpatterns = [
    # path('index/', views.IndexPage().as_view(), name='home'),
    path('bookings/', views.BookingList.as_view(), name='bookings'),
]