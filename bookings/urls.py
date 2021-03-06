from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views


urlpatterns = [
    path('add/', views.make_booking,  name="add_booking"),
    path('manage/', views.manage_booking, name="manage_booking"),
    path('update/<str:pk>/', views.update_booking, name="update_booking"),
    path('delete/<str:pk>/', views.delete_booking, name="delete_booking"),

]

urlpatterns += staticfiles_urlpatterns()
