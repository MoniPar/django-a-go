from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

TYPE_CHOICES = (
    ("Consultation", "Consultation"),
    ("Details & Design", "Details & Design"),
    ("Fabrics", "Fabrics"),
    ("First Fitting", "First Fitting"),
    ("Second Fitting", "Second Fitting"),
    ("Pick-up", "Pick-up"),
)

TIME_CHOICES = (
    ("8:30 AM", "8:30 AM"),
    ("11:30 AM", "11:30 AM"),
    ("4:00 PM", "4:00 PM"),
    ("5:00 PM", "5:00 PM"),
    ("6:00 PM", "6:00 PM"),
)


class Appointment(models.Model):
    user = models.ForeignKey(
        User, related_name="user", on_delete=models.CASCADE)
    type = models.CharField(
        max_length=25, choices=TYPE_CHOICES, default="Consultation")
    date = models.DateField(default=datetime.now)
    time = models.CharField(
        max_length=10, choices=TIME_CHOICES, default="8:30 AM")
    comments = models.TextField()
    submitted = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["submitted"]

    def __str__(self):
        return f"{self.type} | {self.user.username} | Date: {self.date} | "
        f"Time: {self.time}"
