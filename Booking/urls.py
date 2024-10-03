# Booking/urls.py

from django.urls import path
from .views import AppointmentListCreateView, verify_appointment, appointment_confirmed
from . import views


urlpatterns = [
    path('appointments/', AppointmentListCreateView.as_view(), name='appointment-list-create'),
    path('api/book-appointment', views.book_appointment, name='book_appointment'),
    path('verify-appointment/<uidb64>/<token>/', verify_appointment, name='verify_appointment'),
    path('appointment-confirmed/', appointment_confirmed, name='appointment_confirmed'),
]