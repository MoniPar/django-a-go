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
     path('appointments/new', views.AppointmentCreate.as_view(),
          name='appointment-create'),
     path('appointments/<int:pk>/update', views.AppointmentUpdate.as_view(),
          name='appointment-update'),
     path('appointments/<int:pk>/delete', views.AppointmentDelete.as_view(),
          name='appointment-delete'),
]
