from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from django.contrib import messages
from datetime import datetime, timedelta
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


def booking(request):
    # Calls 'validWeekday' function to loop days in the next 21 days
    weekdays = validWeekday(22)
    # Shows only the days that are not full
    validateWeekdays = isWeekdayValid(weekdays)

    if request.method == 'POST':
        type = request.POST.get('type')
        date = request.POST.get('date')
        if type is None:
            messages.error(
                request,
                "Please select the type of appointment you'd like to book"
            )
            return redirect('booking')

        # Stores day and type in Django session
        request.session['date'] = date
        request.session['type'] = type
        return redirect('bookingSubmit')

    return render(request, 'booking.html', {
        'weekdays': weekdays,
        'validateWeekdays': validateWeekdays,
    })


def bookingSubmit(request):
    user = request.user
    times = [
        "8:30 AM", "11:00 AM", "4:00 PM", "5:00 PM", "6:00 PM"
    ]
    today = datetime.now()
    minDate = today.strftime('%d-%m-%Y')
    deltatime = today + timedelta(days=21)
    strdeltatime = deltatime.strftime('%d-%m-%Y')
    maxDate = strdeltatime

    # Gets stored data from Django session
    date = request.session.get('date')
    type = request.session.get('type')

    # Shows the time of the day that hasn't been selected before
    hour = checkTime(times, date)
    if request.method == 'POST':
        time = request.POST.get("time")
        date = dayToWeekday(date)

        if type is not None:
            if date <= maxDate and date >= minDate:
                if Appointment.objects.filter(date=date, time=time).count() < 1:
                    AppointmentForm = Appointment.objects.get_or_create(
                        user=user,
                        type=type,
                        date=date,
                        time=time
                    )
                    messages.success(
                        request, "Appointment saved!"
                    )
                    return redirect('booking')
                else:
                    messages.error(
                        request,
                        "We're sorry but there are no available "
                        "appointments at this time!"
                    )
            else:
                messages.error(
                    request,
                    "We're sorry but we cannot accomodate "
                    "appointments at this date."
                )
        else:
            messages.error(
                request,
                "Please select the type of Appointment"
            )

    return render(request, 'bookingSubmit.html', {
        'times': hour,
    })


# def appointmentList(request):
#     user = request.user
#     appointments = Appointment.objects.filter(user=user).order_by(
#             'date', 'time')
#     return render(request, 'booking/appointments.html', {
#         'user': user,
#         'appointments': appointments
#     })


def appointmentUpdate(request, id):
    appointment = Appointment.objects.get(pk=id)
    userdatepicked = appointment.date
    today = datetime.today()
    minDate = today.strftime('%d-%m-%Y')

    # 24h if statement in template
    delta24 = (userdatepicked).strftime('%d-%m-%Y') >= (today + timedelta(days=1)).strftime('%d-%m-%Y')
    # Calls 'validWeekday' function to loop days in next 21 days
    weekdays = validWeekday(22)
    # Shows only the days that are not full
    validateWeekdays = isWeekdayValid(weekdays)

    if request.method == 'POST':
        type = request.POST.get('type')
        date = request.POST.get('date')

        # Stores type and date in Django session
        request.session['date'] = date
        request.session['type'] = type

        return redirect('appointmentUpdateSubmit', id=id)

    return render(request, 'appointmentUpdate.html', {
        'weekdays': weekdays,
        'validateWeekdays': validateWeekdays,
        'delta24': delta24,
        'id': id
    })


def appointmentUpdateSubmit(request, id):
    user = request.user
    times = [
        "8:30 AM", "11:00 AM", "4:00 PM", "5:00 PM", "6:00 PM"
    ]
    today = datetime.now()
    minDate = today.strftime('%d-%m-%Y')
    deltatime = today + timedelta(days=21)
    strdeltatime = deltatime.strftime('%d-%m-%Y')
    maxDate = strdeltatime

    # Gets stored data from Django session
    date = request.session.get('date')
    type = request.session.get('type')

    # Shows the time of the day that hasn't been selected before
    # and the time user is editing
    hour = checkTime(times, date, id)
    appointment = Appointment.objects.get(pk=id)
    userSelectedTime = appointment.time

    if request.method == 'POST':
        time = request.POST.get("time")
        date = dayToWeekday(date)

        if type is not None:
            if date <= maxDate and date >= minDate:
                if Appointment.objects.filter(date=date, time=time).count() < 1 or userSelectedTime == time:
                    AppointmentForm = Appointment.objects.filter(pk=id).update(
                        user=user,
                        type=type,
                        date=date,
                        time=time
                    )
                    messages.success(
                        request, "Appointment edited!"
                    )
                    return redirect('booking')
                else:
                    messages.error(
                        request,
                        "We're sorry but there are no available "
                        "appointments at this time!"
                    )
            else:
                messages.error(
                    request,
                    "We're sorry but we cannot accomodate "
                    "appointments at this date."
                )
        else:
            messages.error(
                request,
                "Please select the type of Appointment!"
            )
        return redirect('appointmentList')

    return render(request, 'appointmentUpdateSubmit.html', {
        'times': hour,
        'id': id
    })
