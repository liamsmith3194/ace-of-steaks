from django.conf.urls import url
from django.contrib import admin
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^manage', views.manage_bookings),
    url(r'^add', views.book_table),
]


urlpatterns += staticfiles_urlpatterns()