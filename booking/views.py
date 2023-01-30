from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Appointment


class Home(View):

    def get(self, request):
        return render(request, 'home.html', {'title': 'Home'})


class AppointmentList(generic.ListView):
    model = Appointment
    context_object_name = 'appointments'
    template_name = 'booking/appointments.html'
    paginate_by = 6

    # def get_queryset(self):
    #     user = get_obj_or_404(User, username=self.kwargs.get("username"))
    #     return Appointment.objects.filter(user=user).order_by("-submitted")
