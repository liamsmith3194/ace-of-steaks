from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^manage', views.manage_bookings),
    url(r'^add', views.book_table),
]