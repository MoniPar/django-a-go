from django.urls import path, include
from booking import views

urlpatterns = [
    path('', views.Home.as_view(), name='home-page'),
    path('accounts/', include('allauth.urls')),
]
