from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
   path('add/', views.make_booking,  name="add_booking"),
   path('manage/', views.manage_booking, name="manage_bookings"),
   path('update/<str:pk>/', views.update_booking, name="update_booking"),
]

urlpatterns += staticfiles_urlpatterns()