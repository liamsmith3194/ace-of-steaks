from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = ('reference', 'date', 'lname', 'location', 'quantity' )
    prepopulated_fields = {'reference': ('fname', 'lname','location')}
    list_filter = ('location', 'date')
    search_fields = ['fname', 'lname']

    # fields = ['fname', 'lname']

    # fieldsets = (
    #     ('Details', {
    #         'fields': ('fname', 'lname',)
    #     }),
    # )

    # creates dropdown action
    # actions = ['approve_comments']

    # def approve_comments(self, request, queryset):
    #     queryset.update(approved=True)