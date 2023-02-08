from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=25, null=True, blank=False)
    last_name = models.CharField(max_length=32, null=True, blank=False)
    email = models.EmailField(max_length=50, null=True)
    phone = models.CharField(max_length=31, null=True)
    occasion_date = models.DateField(null=True)
    occasion_type = models.CharField(
        max_length=50, null=True)
    occasion_requirement = models.TextField()

    def __str__(self):
        return f'{self.user.username} Profile'

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
