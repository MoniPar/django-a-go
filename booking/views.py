from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic, View
from .models import *


class Home(View):

    def get(self, request):
        return render(request, 'home.html', {'title': 'Home'})


class AppointmentList(generic.ListView):
    model = Appointment
    context_object_name = 'appointments'
    template_name = 'booking/appointments.html'
    ordering = ['date', 'time']
    paginate_by = 6

    def get_queryset(self):
        # user = get_obj_or_404(User, username=self.kwargs.get("username"))
        return Appointment.objects.filter(user=self.request.user)


class AppointmentDetail(generic.DetailView):
    model = Appointment


class AppointmentCreate(LoginRequiredMixin, generic.CreateView):
    model = Appointment
    fields = ['type', 'date', 'time', 'comments']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
