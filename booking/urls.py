from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home-page'),
    path('appointments/', views.AppointmentList.as_view(), name='appointments')
]
