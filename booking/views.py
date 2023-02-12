from django.shortcuts import render, redirect
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)
from django.views import generic, View
from .models import *


class Home(View):

    def get(self, request):
        return render(request, 'home.html', {'title': 'Home'})


class AppointmentList(LoginRequiredMixin, generic.ListView):
    model = Appointment
    context_object_name = 'appointments'
    template_name = 'booking/appointments.html'
    ordering = ['date', 'time']
    paginate_by = 6

    def get_queryset(self):
        return Appointment.objects.filter(user=self.request.user)


class AppointmentDetail(
    LoginRequiredMixin, UserPassesTestMixin, generic.DetailView
):
    model = Appointment

    def test_func(self):
        appointment = self.get_object()
        if self.request.user == appointment.user:
            return True
        return False


class AppointmentCreate(LoginRequiredMixin, generic.CreateView):
    model = Appointment
    fields = ['type', 'date', 'time', 'comments']

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super().form_valid(form)


class AppointmentUpdate(
        LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView
):
    model = Appointment
    template_name = 'booking/appointment_update.html'
    fields = ['type', 'date', 'time', 'comments']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        appointment = self.get_object()
        if self.request.user == appointment.user:
            return True
        return False
