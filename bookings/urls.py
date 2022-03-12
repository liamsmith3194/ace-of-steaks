from django.conf.urls import url
from django.contrib import admin
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^manage', views.ManageBookings),
    url(r'^add', views.BookTable),
]

urlpatterns += staticfiles_urlpatterns()