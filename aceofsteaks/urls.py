from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('bookings/', include('bookings.urls')),
    path('', views.index, name="home"),
    path('menu/', views.menu, name="menu"),
    path('accounts/', include('allauth.urls')),

]
