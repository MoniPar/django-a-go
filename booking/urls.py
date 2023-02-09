from django.urls import path
from .views import AppointmentList, AppointmentDetail
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home-page'),
    # path('appointments/', views.appointmentList, name='appointments'),
    path('appointments/', views.AppointmentList.as_view(),
         name='appointments'),
    path('appointments/<int:pk>/', views.AppointmentDetail.as_view(),
         name='appointment-detail'),
]
