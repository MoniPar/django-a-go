from django.contrib import admin
from .models import Appointment


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = (
        "user", "type", "date", "time",
        "comments", "submitted", "approved"
    )
    list_filter = (
        "date", "type", "approved"
    )
    search_fields = ("user__username", "type", "date")
    actions = ["approve_appointments"]

    def approve_appointments(self, request, queryset):
        queryset.update(approved=True)
